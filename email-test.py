import email


def main() -> None:
    with open("/Users/steve/Downloads/FW_ Payment Received.eml", "rb") as f:
        msg = email.message_from_bytes(f.read())

        for part in msg.walk():
            if part.get_content_type() == "multipart":
                continue

            filename = part.get_filename()
            if filename:
                print(filename)
                with open(f"/Users/steve/Downloads/output/{filename}", "wb") as f:
                    payload = part.get_payload(decode=True)

                    if isinstance(payload, bytes):
                        f.write(payload)
                    else:
                        print("Payload is not bytes.")
            else:
                print("No filename found in the email part.")


if __name__ == "__main__":
    main()

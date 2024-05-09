import subprocess

FILE_NAME = "main"


def run_command():
    try:
        # Execute the command and capture stdout
        result = subprocess.run(
            ["npx", "ts-node", f"/tmp/{FILE_NAME}.ts"],
            stdout=subprocess.PIPE,
            check=True,
        )

        # Print the stdout
        print("Stdout:", result.stdout.decode("utf-8"))
    except subprocess.CalledProcessError as e:
        # Handle error if the subprocess returns non-zero exit status
        print("Error:", e)


# Call the function to run the command
run_command()

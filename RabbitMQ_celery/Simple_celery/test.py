from Simple_celery.tasks import add, hello, background, reverse_string

def invoke_tasks():

    result = add.delay(4, 6)
    print('Task result:', result.get())

    msg = hello.apply_async()
    print(msg.get())

    back = background.delay(4)
    print("Background task return: ", back.get())

    string = reverse_string.delay("Trushali")
    print(f"Reversed String: {string.get()}. Status of task: {string.status}")

if __name__ == '__main__':
    invoke_tasks()
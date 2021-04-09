import psutil


if __name__ == "__main__":
    print("Ein Test output von Python")
    print("\n")
    print("?CPU usage: ", psutil.cpu_percent())
    print("Memory usage: ", psutil.virtual_memory()[2])
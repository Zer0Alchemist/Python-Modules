from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"{result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            data.append(0)
            data.pop()
            if data[0] is None:
                return False
            for key in data:
                int(key)
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        if self.validate(data) is False:
            err = "[ERROR] Invalid type detected: Connection timeout"
            return self.format_output(err)
        else:
            le = len(data)
            if le == 0:
                err = "[ERROR] Empty list detected: Connection timeout!"
                return self.format_output(err)
            m = sum(data)
            avg = m / le
            val = f"Processed {le} numeric values, sum={m}, avg={avg}"
            return self.format_output(val)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            data.upper()
            if data == "":
                return False
            return True
        except AttributeError:
            return False

    def process(self, data: Any) -> str:
        if self.validate(data) is False:
            err = "[ERROR] Invalid type detected: Connection timeout"
            return self.format_output(err)
        else:
            le = len(data)
            word = len(data.split(" "))
            val = f"Processed text: {le} characters, {word} words"
            return self.format_output(val)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        lst = ["INFO", "ERROR"]
        try:
            data.upper()
            if data == "":
                return False
            test = data.upper().split(":", 1)
            if test[0] not in lst:
                return False
            return True
        except Exception as e:
            print(type(e).__name__)
            return False

    def process(self, data: Any) -> str:
        if self.validate(data) is False:
            err = "ERROR Uknown type"
            return self.format_output(err)
        else:
            data_check = data.upper().strip().split(":", 1)
            if data_check[0] == "ERROR":
                val = "[ALERT] ERROR level detected: Connection timeout"
                return self.format_output(val)
            elif data_check[0] == "INFO":
                val = "[INFO] INFO level detected: System ready"
                return self.format_output(val)


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initalizing Numeric Processor...")
    try:
        lst = [1, 2, 3, 4, 5]
        data = NumericProcessor()
        if data.validate(lst) is False:
            raise AttributeError("Validation: Numeric data not verified")
        else:
            print(f"Processing data: {lst}")
            print("Validation: Numeric data verified")
            print(f"Output: {data.process(lst)}")
    except AttributeError as e:
        print(e)

    print("\nInitializing Text Processor...")
    try:
        string = "Hello Nexus World"
        data_str = TextProcessor()
        if data_str.validate(string) is False:
            raise AttributeError("Validation: Text data not verified")
        else:
            print(f"Processing data: \"{string}\"")
            print("Validation: Text data verified")
            print(f"Output: {data_str.process(string)}")
    except AttributeError as e:
        print(e)

    print("\nInitializing Log Processor...")
    try:
        log_info = "ERROR: Connection timeout"
        log = LogProcessor()
        if log.validate(log_info) is False:
            raise AttributeError("Validation: Log entry not verified")
        else:
            print(f"Processing data: \"{log_info}\"")
            print("Validation: Log entry verified")
            print(f"Output: {log.process(log_info)}")
    except AttributeError as e:
        print(e)

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface")

    print("Result1:", data.process([2, 2, 2]))
    print("Result2:", data_str.process("Hello World!"))
    print("Result3:", log.process("INFO"))

    print("\nFoundation systems online. Nexus ready for advanced streams.")

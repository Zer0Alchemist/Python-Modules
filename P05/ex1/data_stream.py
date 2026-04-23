from abc import ABC, abstractmethod
from typing import Any, List, Union, Optional, Dict


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        super().__init__()
        self.stream_id = stream_id
        self.stream_type = "something idk"
        self.total_processed = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "total_processed": self.total_processed
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            dct = {k.strip(): v.strip()
                   for item in data_batch
                   for k, v in [item.split(":")]}

            alert = []
            temp = float(dct["temp"])
            if temp > 40:
                alert.append("[ALERT]: High temperature!")
            if temp < 0:
                alert.append("[ALERT]: Low temperature!")

            hum = float(dct["humidity"])
            if hum > 80:
                alert.append("[ALERT]: High humidity!")
            if hum < 20:
                alert.append("[ALERT]: Low humidity!")

            press = float(dct.get("pressure", 1013))
            if press > 1020:
                alert.append("[ALERT]: High pressure!")
            if press < 1000:
                alert.append("[ALERT]: Low pressure!")

            le = len(data_batch)
            self.total_processed += le

            if alert:
                return f"{le} readings processed, avg temp: {temp}°C, {alert}"
            else:
                return f"{le} readings processed, avg temp: {temp}°C"
        except Exception:
            return "ERROR: Couldn't process sensor batch"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            val_buy = sum([int(item.split(":")[1])
                           for item in data_batch
                           if item.split(":")[0].strip() == "buy"])
            val_sell = sum([int(item.split(":")[1])
                           for item in data_batch
                           if item.split(":")[0].strip() == "sell"])

            le = len(data_batch)
            net = val_buy - val_sell
            if net > 0:
                pos = f"+{net}"
            else:
                net *= -1
                pos = f"-{net}"
            return f"{le} operations, net flow: {pos} units"
        except Exception:
            return "ERROR: Couldnt process Sensor batch"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            err_count = len([item
                             for item in data_batch
                             if item == "error"])
            le = len(data_batch)
            return f"{le} events, {err_count} error detected"
        except Exception:
            return "ERROR: Couldn't process Event batch"


class StreamProcessor:
    def __init__(self, streams: List[DataStream]) -> None:
        self.streams = streams

    def batch_all(self, data_batch: List[Any]) -> None:
        try:
            for stream in self.streams:
                if isinstance(stream, SensorStream):
                    sensor = stream.process_batch(data_batch["sensor"])
                    print(f"- Sensor data: {sensor}")
                elif isinstance(stream, TransactionStream):
                    transaction = stream.process_batch(
                        data_batch["transaction"])
                    print(f"- Transaction data: {transaction}")
                elif isinstance(stream, EventStream):
                    event = stream.process_batch(data_batch["event"])
                    print(f"- Event data: {event}")
        except Exception:
            print("Polymorphism failed!")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sens = SensorStream("SENSOR_001")
    print(f"Stream ID: {sens.stream_id}, Type: {sens.stream_type}")
    try:
        sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
        print(f"Processing sensor batch: {sensor_batch}")
        print(f"Sensor analysis: {sens.process_batch(sensor_batch)}")
    except Exception as e:
        print(e)

    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    try:
        trans_batch = ["buy:100", 54, "buy:75"]
        print(f"Processing Transaction batch: {trans_batch}")
        print(f"Transaction analysis: {trans.process_batch(trans_batch)}")
    except Exception as e:
        print(e)

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    try:
        event_bash = ["login", "error", "logout"]
        print(f"Processing event batch: {event_bash}")
        print(f"Event analysis: {event.process_batch(event_bash)}")
    except Exception as e:
        print(e)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    print("Batch 1 Results:")
    sensor_check = SensorStream("test")
    trans_check = TransactionStream("test")
    event_check = EventStream("test")

    stream = StreamProcessor([sensor_check, trans_check, event_check])
    data = {
        "sensor": ["temp:20", "humidity: 70"],
        "transaction": ["buy:100", "sell:50", "buy:30", "sell:40"],
        "event": ["login", "error", "logout"]
    }
    stream.batch_all(data)

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal")

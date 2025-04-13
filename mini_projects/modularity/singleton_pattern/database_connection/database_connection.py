class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("[Database Connection] Membuat Instance Baru...")
            cls._instance = super().__new__(cls)
            cls._instance.log = []
        return cls._instance

    def connect(self):
        self._instance.log.append("DB Connected")

    def disconnect(self):
        self._instance.log.append("DB Disconnected")

    def tampilkan_log(self):
        for x in self._instance.log:
            print(f"[LOG] {x}")

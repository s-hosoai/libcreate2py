



## 検討項目
- 採　PythonでCのbyte[] -> Structと同じことが可能か
- 没　Pythonから渡したbyte[]をCでStructに変換して返す

Structure.from_buffer_copy()で解決．
serial.read()したデータから直接生成可能．

- SensorObserverの実装
- SensorObserverからイベント生成
- OpCode周りの移植
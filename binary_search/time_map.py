from collections import defaultdict


class TimeMap:

    def __init__(self):
        self._kv = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._kv:
            self._kv[key] = [(value, timestamp),]
        else:
            self._kv[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        keys = self._kv.get(key, [])
        res = ""
        l, r = 0, len(keys)-1
        k: int
        while l <= r:
            k = (l+r) >> 1
            if keys[k][1] <= timestamp:
                l = k + 1
                res = keys[k][0]
            else:
                r = k - 1
        return res


if __name__ == "__main__":
    tmap = TimeMap()
    tmap.set("love", "high", 10)
    tmap.set("love", "low", 20)
    print(tmap.get("love", 5))
    print(tmap.get("love", 10))
    print(tmap.get("love", 15))
    print(tmap.get("love", 20))
    print(tmap.get("love", 25))

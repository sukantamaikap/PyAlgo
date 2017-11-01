import array


class Searches:

    def binary_search(self, ar, key):
        """ search from array ar for the key k, it should be sorted, otherwise, the behavior is unpredictable"""
        if not isinstance(ar, type(array)):
            print('wrong instance passed, pass an array for search')
        print("assumption : the input array should be sorted !!!")
        low = 0
        high = len(ar) - 1
        while low <= high:
            mid = int((low + high) / 2)
            print('mid index being inspected : ', mid)
            if ar[mid] == key:
                return key
            if ar[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        return None


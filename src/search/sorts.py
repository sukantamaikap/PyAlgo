"""all sorting algorithm implementation"""class Sorts:    def quick_sort(self, ar):        """quick sort implementation"""        if len(ar) < 2:            return ar        else:            pivot = ar[0]            print("pivot is : ", pivot)            less = [i for i in ar[1:] if i <= pivot]            more = [i for i in ar[1:] if i > pivot]            return self.quick_sort(less) + [pivot] + self.quick_sort(more)
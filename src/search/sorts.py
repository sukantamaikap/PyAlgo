from random import shuffle"""all sorting algorithm implementation"""class Sorts:    def quick_sort(self, elements):        """quick sort implementation"""        if len(elements) < 2:            return elements        else:            shuffle(elements)            pivot = elements[0]            print("pivot is : ", pivot)            less = [i for i in elements[1:] if i <= pivot]            more = [i for i in elements[1:] if i > pivot]            return self.quick_sort(less) + [pivot] + self.quick_sort(more)
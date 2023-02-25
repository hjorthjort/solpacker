import copy

class Bin:
    size = 0
    elems = []
    
    def __init__(self):
        self.size = 0
        self.elems = []

    def add(self, elem, size):
        self.elems.append(elem)
        self.size += size

    def delete(self, elem, size):
        self.elems.remove(elem)
        self.size -= size

    def __str__(self):
        return "(%.3s) %s" % (str(self.size), str(self.elems))
    
    def __repr__(self):
        return self.__str__()

# For keeping track of recursion depth, debugging help.
_rec_count = 0

def pack(items_sizes, bin_capacity, num_to_beat=256, good_enough=None):
    """Recusive bin packing algorithm. Beware that this is an exponential time algorithm. Call with care.
    :param items_sizes: list of items to be packed, as a dictionary of label and size
    :param bin_capacity: capacity of each bin
    :param num_to_beat: number of bins to beat
    :return: list of bins, each containing a list of items
    """

    if len(items_sizes) == 0:

        return [Bin()]

    # Sort items by size, largest first
    # This guarantees that the left spine of the recision tree will implement the first fit heuristic.
    items_sorted = sorted(items_sizes, key=lambda x: items_sizes[x], reverse=True)

    theoretical_limit = (bin_capacity - 1 + sum([items_sizes[x] for x in items_sorted])) // bin_capacity
    if good_enough is None or good_enough < theoretical_limit:
        good_enough = theoretical_limit
  
    def pack_aux(items, num_to_beat, bins):
        """Recursive helper function for pack().
        :param items: list of items to be packed, as list of labels
        :param num_to_beat: number of bins to beat
        :param bins: list of bins, each containing a list of items
        :return: list of bins, each containing a list of items
        """

        global _rec_count

        bins = copy.deepcopy(bins)
        best_size = num_to_beat

        if len(items) == 0:
            if len(bins) < num_to_beat:
                return bins
            return None

        best_solution = None

        # Try to pack the first item into an existing bin
        # We modify the list of bins in place, so we need to restore it to its original state
        for bin in bins:
            if bin.size + items_sizes[items[0]] <= bin_capacity:
                bin.add(items[0], items_sizes[items[0]])
                _rec_count += 1
                new = pack_aux(items[1:], best_size, bins)
                _rec_count -= 1
                bin.delete(items[0], items_sizes[items[0]])
                if new is not None and len(new) == good_enough:
                    return new
                if new is not None and len(new) < best_size:
                    best_size = len(new)
                    best_solution = new
        # Don't try adding more bins if that would mean we have more bins than the best solution so far
        if len(bins) >= best_size:
            return best_solution

        # In addition to trying with the first item in all existing bins, try to also give it a fresh bin.
        fresh_bin = Bin()
        fresh_bin.add(items[0], items_sizes[items[0]])

        bins.append(fresh_bin)
        _rec_count += 1
        new = pack_aux(items[1:], best_size, bins)
        _rec_count -= 1
        if new is not None and len(new) == good_enough:
            return new
        if new is not None and len(new) < best_size:
            best_size = len(new)
            best_solution = new

        return best_solution

    rec = pack_aux(items_sorted, num_to_beat, [])
    return rec
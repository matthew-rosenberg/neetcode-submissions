from collections import Counter, defaultdict, namedtuple

Word_data = namedtuple('Word_data', ['word', 'counter'])
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_groups = []
        for s in strs:
            c = Counter(s)
            word_data = Word_data(s, c)

            added = False
            print(s)
            for counter_group in counter_groups:
                print(counter_group)
                if c == counter_group[0].counter:
                    counter_group.append(word_data)
                    added = True
                    break
            if not added:
                counter_groups.append([word_data])
        # Process
        print('\ncounter groups', counter_groups)
        output = []
        print('\noutput', output)
        for counter_group in counter_groups:
            output.append([word_data.word for word_data in counter_group])
        return output
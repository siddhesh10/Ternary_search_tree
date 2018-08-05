import sys
sys.path.insert(0, 'C:/Users/sidd/Desktop/ternary_search_tree/')
import ternary_search_tree

mytst = ternary_search_tree.trie('cute')

mytst.append('cup')
#ytst.put("hello",200)
#mytst.put("welcome",300)
print(mytst.contains('cup'))

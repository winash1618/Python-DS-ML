from NumpyCreator import NumPyCreator
npc = NumPyCreator()
npc.from_list([[1,2,3],[6,3,4]])
# Output :
# array([[1, 2, 3], [6, 3, 4]])
npc.from_list([[1,2,3],[6,4]])
# # Output :
# # None
npc.from_list([[1,2,3],['a','b','c'],[6,4,7]])
# # Output :
# # array(['1','2','3'],['a','b','c'],['6','4','7'], dtype='<U21')
npc.from_list(((1,2),(3,4)))
# # Output :
# # None
npc.from_tuple(("a", "b", "c"))
# # Output :
# # array(['a', 'b', 'c'])
npc.from_tuple(["a", "b", "c"])
# # Output :
# # None
npc.from_iterable(range(5))
# # Output :
# # array([0, 1, 2, 3, 4])
shape=(3,5)
npc.from_shape(shape)
# # Output :
# # array([[0, 0, 0, 0, 0],
# # [0, 0, 0, 0, 0],
# # [0, 0, 0, 0, 0]])
npc.random(shape)
# # Output :
# # array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768 ],
# # [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
# # [0.79585328, 0.00660962, 0.92910958, 0.9905421 , 0.05244791]])
npc.identity(4)
# # Output :
# # array([[1., 0., 0., 0.],
# # [0., 1., 0., 0.],
# # [0., 0., 1., 0.],
# # [0., 0., 0., 1.]])
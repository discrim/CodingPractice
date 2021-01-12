def vector_addition(*vectors):
  print('vectors: ', vectors)
  print('*vectors: ', *vectors)
  print('*zip(vectors): ', *zip(vectors))
  print('*zip(*vectors): ', *zip(*vectors))
  return [sum(i) for i in zip(*vectors)]

if __name__ == '__main__':
  v1 = ([1, 3], [2, 4], [6, 7])
  print(vector_addition(*v1))
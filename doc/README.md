# Task #1

## Vectors

- Vectors addition
- Lineal transformation with an image
- Rotate
- Tighten
- Stretch 

## Matrix
- Matrix multiplication
- 2 transformations of associated matrices


# Task #2

- Prove that any rotational-only transformation matrix has determinant 1
- Try the intuition of the determinant with different transformation in Jupyter Notebooks. Including the "cat/fun" transformation
- Provide a transformation that increases the area of the transformation space by "K" (Choose whatever "K" you want except 1), then compute the area in both spaces and confirm the concept (Use Jupyter Notebooks)
- This is a basis in 3D. With the corresponding vectors ((Exercises figure at point 4)[./clase.excalidraw]) $i$, $j$, $k$; define the following transformations as python functions. You provide the function with the angle parameter $\theta$ and it returns the transformation
    - a) Rotation by $\theta$ degrees on $x$ axis
    - b) Rotation by $\theta$ degrees on $y$ axis
    - c) Rotation by $\theta$ degrees on $z$ axis

- Now provide a function that given 3 arguments representing angles on $x$, $y$ and $z$ respectively returns a combinaed transformation. Try it with different vectors and confirm your results
- Provide a different  transformation and confirm that what returned function of point 5 has always zero determinant
- Provide a transformation that takes any vector of the 3D space and projects it to the light-blue plane. Compute the determinant
- Provide a transformation that takes any vector of the 3D space and takes it to the purple line. What is your conclusion about the determinant?
- The easiest one: Provide a transformation of a vector in the 3D space and transforms it to the vector $\vec([0, 0 k])$ for any constant $k$. Provide your conclusions on the determinant

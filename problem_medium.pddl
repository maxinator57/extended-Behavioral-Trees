(define (problem medium)
    (:domain medium)
    
    (:objects
        cube1 cube2 cube3 cube4
        A B C
    )
    
    (:init
        (conn A B)
        (conn B A)
        (conn B C)
        (conn C B)
        (in cube1 A)
        (in cube2 B)
        (in cube3 B)
        (in cube4 C)
    )
    
    (:goals
        (move cube1 A A B)
        (move cube2 B C A)
        (move cube3 B A C)
        (move cube4 C A B)
    )
)
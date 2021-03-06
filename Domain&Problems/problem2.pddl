(define (problem_2)
    (:domain cubes)
    
    (:objects
        cube1 cube2 cube3 cube4
        A B C
    )
    
    (:init
        (conn A B)
        (conn B A)
        (conn B C)
        (conn C B)
        (robot_in B)
        (in cube1 A)
        (in cube2 B)
        (in cube3 B)
        (in cube4 C)
    )
    
    (:goals
        (transport cube1 A B A B C)
        (transport cube2 B C A B C)
    )
)
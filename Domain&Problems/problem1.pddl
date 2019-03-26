(define (problem_1)
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
    )
    
    (:goals
        (get_to A A B C)
    )
)
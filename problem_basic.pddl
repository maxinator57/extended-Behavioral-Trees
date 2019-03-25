(define (problem basic)
    (:domain basic)
    
    (:objects
        cube1 cube2 cube3
        A B C
    )
    
    (:init
        (is_A A)
        (is_B B)
        (is_C C)
        (conn A B)
        (conn B C)
        (in cube1 A)
        (in cube2 B)
        (in cube3 B)
    )
    
    (:goals
        (get_to_C cube1 A C B)
        (get_to_C cube2 B C A)
    )
)
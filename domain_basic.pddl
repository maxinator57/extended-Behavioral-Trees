(define (domain basic)

  (:predicates
  (in ?obj ?loc)
  (conn ?loc1 ?loc2)
  (is_A ?loc)
  (is_B ?loc)
  (is_C ?loc))
    
(:tasks
    (move_simple)
    (get_to_C)
)

(:operator move_simple
 :parameters (?obj ?loc1 ?loc2)
 :task (move_simple ?obj ?loc1 ?loc2)
 :precondition ((in ?obj ?loc1) (conn ?loc1 ?loc2))
 :effect (and (not (in ?obj ?loc1)) (in ?obj ?loc2))
)

(:method move_complex_B_to_C
 :parameters (?obj ?loc1 ?loc2 ?loc3)
 :task (get_to_C ?obj ?loc1 ?loc2 ?loc3)
 :precondition ((is_B ?loc1) (is_C ?loc2) (in ?obj ?loc1))
 :subtasks ((move_simple ?obj ?loc1 ?loc2))
)

(:method move_complex_A_to_C
 :parameters (?obj ?loc1 ?loc2 ?loc3)
 :task (get_to_C ?obj ?loc1 ?loc2 ?loc3)
 :precondition ((is_A ?loc1) (is_C ?loc2) (in ?obj ?loc1))
 :subtasks ((move_simple ?obj ?loc1 ?loc3) (move_simple ?obj ?loc3 ?loc2))
)

)
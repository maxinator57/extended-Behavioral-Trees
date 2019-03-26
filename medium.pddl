(define (domain medium)

  (:predicates
  (in ?obj ?loc)
  (conn ?loc1 ?loc2)
  )
    
(:tasks
    (move)
    (move_simple)
    ()
)

(:operator move_simple_op
 :parameters (?obj ?loc1 ?loc2)
 :task (move_simple ?obj ?loc1 ?loc2)
 :precondition ((in ?obj ?loc1) (conn ?loc1 ?loc2))
 :effect (and (not (in ?obj ?loc1)) (in ?obj ?loc2))
)

(:method move_simple_mtd
 :parameters (?obj ?loc1 ?loc2 ?loc3)
 :task (move ?obj ?loc1 ?loc2 ?loc3)
 :precondition ((conn ?loc1 ?loc2) (in ?obj ?loc1))
 :subtasks ((move_simple ?obj ?loc1 ?loc2))
)

(:method move_complex_mtd
 :parameters (?obj ?loc1 ?loc2 ?loc3)
 :task (move ?obj ?loc1 ?loc2 ?loc3)
 :precondition ((conn ?loc1 ?loc3) (conn ?loc3 ?loc2) (in ?obj ?loc1))
 :subtasks ((move_simple ?obj ?loc1 ?loc3) (move_simple ?obj ?loc3 ?loc2))
)

)
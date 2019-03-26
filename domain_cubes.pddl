(define (domain medium)

  (:predicates
  (in ?obj ?loc)
  (robot_in ?loc)
  (conn ?loc1 ?loc2)
  (loaded ?obj)
  )
    
(:tasks
    (move)
    (move_simple)
    (get_to)
    (transport)
    (load)
    (drop)
)

(:method do_nothing_move_mtd
 :parameters (?loc1 ?loc2 ?const1 ?const2 ?const3)
 :task (move ?loc1 ?loc2 ?const1 ?const2 ?const3)
 :precondition ((robot_in ?loc2))
 :subtasks (())
)

(:method move_simple_mtd
 :parameters (?loc1 ?loc2 ?const1 ?const2 ?const3)
 :task (move ?loc1 ?loc2 ?const1 ?const2 ?const3)
 :precondition ((conn ?loc1 ?loc2) (robot_in ?loc1))
 :subtasks ((move_simple ?loc1 ?loc2))
)

(:method move_complex1_mtd
 :parameters (?loc1 ?loc2 ?const1 ?const2 ?const3)
 :task (move ?loc1 ?loc2 ?const1 ?const2 ?const3)
 :precondition ((conn ?loc1 ?const1) (conn ?const1 ?loc2) (robot_in ?loc1))
 :subtasks ((move_simple ?loc1 ?const1) (move_simple ?const1 ?loc2))
)

(:method move_complex2_mtd
 :parameters (?loc1 ?loc2 ?const1 ?const2 ?const3)
 :task (move ?loc1 ?loc2 ?const1 ?const2 ?const3)
 :precondition ((conn ?loc1 ?const2) (conn ?const2 ?loc2) (robot_in ?loc1))
 :subtasks ((move_simple ?loc1 ?const2) (move_simple ?const2 ?loc2))
)

(:method move_complex3_mtd
 :parameters (?loc1 ?loc2 ?const1 ?const2 ?const3)
 :task (move ?loc1 ?loc2 ?const1 ?const2 ?const3)
 :precondition ((conn ?loc1 ?const3) (conn ?const3 ?loc2) (robot_in ?loc1))
 :subtasks ((move_simple ?loc1 ?const3) (move_simple ?const3 ?loc2))
)

(:operator move_simple_op
 :parameters (?loc1 ?loc2)
 :task (move_simple ?loc1 ?loc2)
 :precondition ((robot_in ?loc1) (conn ?loc1 ?loc2))
 :effect (and (not (robot_in ?loc1)) (robot_in ?loc2))
)

(:method get_to1_mtd
 :parameters (?loc1 ?const1 ?const2 ?const3)
 :task (get_to ?loc1 ?const1 ?const2 ?const3)
 :precondition (())
 :subtasks ((move ?const1 ?loc1 ?const1 ?const2 ?const3))
)

(:method get_to2_mtd
 :parameters (?loc1 ?const1 ?const2 ?const3)
 :task (get_to ?loc1 ?const1 ?const2 ?const3)
 :precondition (())
 :subtasks ((move ?const2 ?loc1 ?const1 ?const2 ?const3))
)

(:method get_to3_mtd
 :parameters (?loc1 ?const1 ?const2 ?const3)
 :task (get_to ?loc1 ?const1 ?const2 ?const3)
 :precondition (())
 :subtasks ((move ?const3 ?loc1 ?const1 ?const2 ?const3))
)

(:method do_nothing_transport_mtd
 :parameters (?obj ?loc1 ?loc2 ?const1 ?const2 ?const3)
 :task (transport ?obj ?loc1 ?loc2 ?const1 ?const2 ?const3)
 :precondition ((in ?obj ?loc2))
 :subtasks (())
)

(:method transport_mtd
 :parameters (?obj ?loc1 ?loc2 ?const1 ?const2 ?const3)
 :task (transport ?obj ?loc1 ?loc2 ?const1 ?const2 ?const3)
 :precondition ((in ?obj ?loc1) (not (in ?obj ?loc2)))
 :subtasks ((get_to ?loc1 ?const1 ?const2 ?const3) (load ?obj ?loc1) (move ?loc1 ?loc2 ?const1 ?const2 ?const3) (drop ?obj ?loc2))
)

(:operator load_op
 :parameters (?obj ?loc1)
 :task (load ?obj ?loc1)
 :precondition ((robot_in ?loc1) (in ?obj ?loc1))
 :effect (and (not (in ?obj ?loc1)) (loaded ?obj))
)

(:operator drop_op
 :parameters (?obj ?loc1)
 :task (drop ?obj ?loc1)
 :precondition ((robot_in ?loc1) (loaded ?obj))
 :effect (and (in ?obj ?loc1) (not (loaded ?obj)))
)

)
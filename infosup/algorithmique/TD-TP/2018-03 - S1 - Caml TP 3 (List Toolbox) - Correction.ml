(***********************  BASICS ON LISTS  *************************)

(* length *)

let rec length = function
    [] -> 0
  | _::l -> 1 + length l ;;

(* product *)

let rec product = function
    [] -> 1
  | e::l -> e * product l;;
(* val produit : int list -> int = <fun> *)


(* nth *)

let nth n list =  
  if n < 0 then
    invalid_arg "nth: index must be a natural"
  else
    let rec nth_rec = function
      | ([], _) -> failwith "nth: list is too short"
      | (e::_, 0) -> e
      | (_::l, n) -> nth_rec (l, n-1)
    in
      nth_rec (list, n) ;;

(* search_pos *)

let rec search_pos x = function
    [] -> failwith "search_pos: not found"
  | e :: l -> (if e = x then 0 else 1) + search_pos x l ;;


(* int_of_bigint *)

let rec int_of_bigint = function
    [] -> 0
  | e::l -> e + 10 * int_of_bigint l ;;

(* prefix *)

let rec prefix = function
    ([], _) | (_, []) -> true
  | (e1::l1, e2::l2) -> e1 = e2 && prefix (l1, l2) ;;

(***********************  BUILD / MODIFY LISTS  *************************)

(* init_list *)
  
let init_list n value =
  if n < 0 then
    invalid_arg "init_list: n must be a natural"
  else 
    let rec build = function
      | 0 -> []
      | n -> value :: build (n-1)
    in
      build n ;;

(* put_list *)

let put_list v i list =
  if i < 0 then
    invalid_arg "put_list: index must be a natural"
  else
    let rec put = function
      | (_, []) -> []
      | (0, _::l) -> v :: l
      | (n, e::l) -> e :: (put ((n-1), l))
    in
      put (i, list) ;;

(* bigint_of_int *)

let bigint_of_int n =
  if n < 0 then
    invalid_arg "bigint_of_int: not a natural"
  else
    let rec tolist n =
      if n = 0 then 
        [] 
      else
        (n mod 10) :: tolist (n / 10)
    in
      tolist n ;;



(***********************  LIST LISTS  *************************)

(* init_board: generate a nblines x nbcolumn  matrix filled with x *)

let init_board (nblines, nbcolumns) x =
  if nblines <= 0 || nbcolumns <= 0 then
    invalid_arg "init_board: one dimension not a non-zero natural"
  else
    init_list nblines (init_list nbcolumns x) ;;


(* get_cell: extract value at position (x, y) from an 'a list list *)

let get_cell (x, y) board =
  nth y (nth x board) ;;


(* put_cell: replace value at (x,y) in board by cell (no "out of bound" test!) *)

let put_cell cell (x, y) board =
  let rec process_row = function
    | (_, []) -> []
    | (0, l::ll) -> (put_list cell y l) :: ll
    | (n, l::ll) -> l :: (process_row ((n-1), ll))
  in
    process_row (x, board);;


(* count_neighbours: extract number of non 0 cells around cell at (x,y) 
   from a lines x columns board  *)


let count_neighbours (x,y) board (lines, columns) = 
  let add (x,y) = 
    if x >= 0 && x < lines && y >= 0 && y < columns then
      get_cell (x,y) board
    else
      0
  in
      add (x-1,y-1) + add (x-1,y) + add (x-1,y+1)
    + add (x,y-1) + add (x,y+1)
    + add (x+1,y-1) + add (x+1,y) + add (x+1,y+1) ;;


(*   examples *)

let board = init_board (5, 3) 0 ;;
let board = put_cell 1 (0, 0) board ;;
let board = put_cell 2 (2, 1) board ;;
get_cell (2, 1) board ;;
count_neighbours (1, 0) board (5, 3) ;;

let board2 = init_board (3, 4) 1 ;;
count_neighbours (1, 2) board2 (3, 4) ;;
count_neighbours (2, 3) board2 (3, 4) ;;

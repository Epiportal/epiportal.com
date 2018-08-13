(* sum l returns the sum of elements in L *)
let rec sum l =
  match l with
      [] -> 0
    | e::l -> e + sum l ;;

(* count x l calculates the number of x in l *)

let rec count x l = match l with
    [] -> 0
  | e::l when x = e -> 1 + count x l
  | _::l -> count x l ;;

let rec count x = function
    [] -> 0
  | e::l -> (if x = e then 1 else 0) + count x l ;;

(* same in a sorted list (not in tuto) *)

let rec count_sorted x = function
    [] -> 0
  | e::l when e > x -> 0
  | e::l -> (if x = e then 1 else 0) + count_sorted x l ;;

(* search x l tests whether x is present in the list l  *)

let rec search x = function
    []            -> false
  | e::l when e = x -> true
  | e::l          -> search x l;;   

let rec search2 x = function
    []   -> false
  | e::l -> (e = x) || (search2 x l) ;;


(* nth i l returns the value at rank i in the list l *)

let nth rank list =
  if rank <= 0 then
     invalid_arg "nth: rank <= 0"
  else
     let rec nth_rec = function
           (_, []) -> failwith "nth: rank > length"
         | (1, e::l) -> e
         | (i, e::l) -> nth_rec (i-1, l)
      in
          nth_rec (rank, list) ;;


(* search_max l returns the maximum value of the list l *)

let rec search_max = function
  | e::[] -> e
  | e::l -> let max = search_max l in
	      if e > max then e else max
  | [] -> failwith "search_max: empty list" ;;

search_max [1; 5; 9; 0] ;;

(******************************************************************)

(* 2.1 arith_list n a1 r builds the list of first n elements
   of the arithmetic progression from a1 and of common ratio r.
*)

let arith_list n a1 r = 
  if n < 1 then
    invalid_arg "arith_list: invalid number of terms"
  else
    let rec build a i = 
      if i > n then
	[]
      else
	a :: build (a+r) (i+1)
    in
    build a1 1 ;;

arith_list 12 2 1 ;;
arith_list 11 0 3 ;;

(* 2.2 append l1 l2 is l1 @ l2 *)

let append l1 l2 =
  if l2 = [] then
     l1
  else
     let rec append_rec = function
         [] -> l2
       | e::l -> e :: append_rec l l2
     in
     append_rec l1 ;;

(**************************************************************)

(* growing l tests whether the list l is sorted by increasing order *)

let rec growing = function
    [] | _::[] -> true
  | e1::e2::l -> e1 <= e2 && growing (e2::l) ;;

(* search x l tests whether x is present in the sorted list l  *)

let rec search x = function
    []            -> false
  | e::l when e = x -> true
  | e::l when e > x -> false
  | e::l          -> search x l;;   

let rec search2 x = function
    []   -> false
  | e::l -> (e = x) || (e < x && search2 x l) ;;

(* remove x l deletes the first x found in the sorted list l *)

let rec remove x = function
    [] -> []
  | e::l when e > x -> e::l
  | e::l when e = x -> l
  | e::l -> e::remove x l ;;

(* insert x l adds the element x at its place in the sorted list l *)

let rec insert x = function
    []   -> [x]
  | e::l -> if x <= e then
                x::e::l
            else
                e::insert x l ;;

(* 2.5 reverse l reverses the elements in l *)

let rec reverse_with_append = function
    []   -> []
  | e::l -> reverse_with_append l @ [e] ;;

let reverse list =
  let rec rev accu = function
      []   -> accu
    | e::l -> rev (e::accu) l
  in rev [] list ;;  

(* test both with long list: at least 20000 elts *)

let rec build = function
  | 0 -> []
  | n -> n :: build (n-1) ;;

(************************************************************************)
(* equal *)

let rec equal list1 list2 =
   match (list1,list2) with
     ([], []) -> true
   | ([], _) | (_, []) -> false
   | (e1::l1, e2::l2) -> e1 = e2 && equal l1 l2 ;;  
   

(* merge *)

let rec merge2 liste1 liste2 =
  match (liste1, liste2) with
    ([], l) | (l, []) -> l
  | (e1::l1, e2::l2) -> 
      if e1 = e2 then 
	e1::(merge2 l1 l2)
      else 
	if e1 < e2 then 
	  e1::(merge2 l1 liste2)
	else 
	  e2::(merge2 liste1 l2) ;;

merge2 [1;5;6;8;9;15] [2;3;4;5;7;9;10;11];;


;; Extra Scheme Questions ;;

; Q5
(define (square x) (* x x))

(define (pow b n)
  (cond ((= n 0) 1)
        ((even? n) (square (pow b (/ n 2))))
        ((odd? n) (* b (square (pow b (/ (- n 1) 2)))))
  )
)

; Q6
(define lst
  (list (list 1) 2 (cons 3 4) 5)
)

; Q7
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q8
(define (remove item lst)
  (if (null? lst)
      nil
      (
      if (= (car lst) item)
      (remove item (cdr lst))
      (cons (car lst) (remove item (cdr lst)))
      )
  )
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q9
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (if (= (min a b) 0)
     (max a b)
     (if (= (modulo (max a b) (min a b)) 0)
         (min a b)
          (gcd (min a b) (modulo (max a b) (min a b)))
     )
  )
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q10
(define (no-repeats s)
  (if (null? s)
      nil
      (
      cons (car s) (no-repeats (filter (lambda (x) (not (= x (car s)))) s))
      )
  )
)


(define (filter f lst)
  (if (null? lst)
      nil
      (if (f (car lst))
      (cons (car lst) (filter f (cdr lst)))
      (filter f (cdr lst))
      )
  )
)


; Q11
(define (substitute s old new)
  (if (null? s)
      nil
      (if (pair? (car s))
          (cons (substitute (car s) old new) (substitute (cdr s) old new))
          (if (eq? (car s) old)
              (cons new (substitute (cdr s) old new))
              (cons (car s) (substitute (cdr s) old new))
          )
      )
  )
)

; Q12

(define (change e olds news)
  (if (null? olds)
      e
      (if (eq? (car olds) e)
          (car news)
          (change e (cdr olds) (cdr news))
      )
  )
)

(define (sub-all s olds news)
  (if (null? s)
      nil
      (if (pair? (car s))
          (cons (sub-all (car s) olds news) (sub-all (cdr s) olds news))
          (cons (change (car s) olds news) (sub-all (cdr s) olds news))
      )
  )
)
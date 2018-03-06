; Primitives

5
3.14
#t  ; or True, or true
#f  ; or False, or false


; Call expressions

(+ 1 2 3 4)
(+)
(*)
(- 12)
(- 20 1 2 3 4 5)
(/ (+ (* (- (* 2 2 2 2 2 3 3 3) 1) 7) 7) 3)
(quotient (+ 8 7) 5)
(+ (* 3
      (+ (* 2 4)
         (+ 3 5)))
   (+ (- 10 7)
      6))


; Definitions

(define a 5)
(define b (+ a 4))


; Symbols

(quote a)  ; or 'a
(define c (define a 3))


; Lambdas

((lambda (x) (* x x)) 4)
(define square (lambda (x) (* x x)))
(define (square x) (* x x))
(define (average x y) (/ (+ x y) 2))


; Conditionals and Booleans

(define (abs x)
  (if (< x 0)
      (- x)
      x))
(define (sgn x)
  (cond ((< x 0) -1)
        ((= x 0) 0)
        (else 1)))
(and False (/ 1 0) 5)
(or True (/ 1 0) 5)


; Pairs

(define x (cons 1 3))
(car x)
(cdr x)
(define x (cons 1 (cons 2 (cons 3 nil))))
(define x (list 1 2 3))
(define x '(1 2 3))


; Coding Practice

; map in Python:
; def map(fn, lnk):
;     if lnk == Link.empty:
;         return Link.empty
;     return Link(fn(lnk.first), map(fn, link.rest))
(define (map fn lst)
  (if (null? lst)
      nil
      (cons (fn (car lst)) (map fn (cdr lst)))))
(map square (list 1 2 3))
(map abs '(-2 -1 0 1 2))

(define (tree entry children)
  (cons entry children))

(define (entry tree) (car tree))

(define (children tree) (cdr tree))

(define (leaf? tree) (null? (children tree)))

(define (square-tree t)
  (tree (square (entry t))
        (if (leaf? t)
            nil
            (map square-tree (children t)))))
(define squared
  (square-tree (tree 3
                     (list
                     (tree 1 nil)
                     (tree 2
                           (list
                           (tree 1 nil)
                           (tree 1 nil)))))))
(entry squared)
(entry (car (children squared)))

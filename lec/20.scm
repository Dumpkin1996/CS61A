;;; Scheme II

;; The let Special Form

(define x 1)
; expect x

(let ((x 10) (y 20)) (+ x y))
; expect 30

x
; expect 1

(let ((x 10) (y x)) (+ x y))
; expect 11


;;; Tail Recursion

;; Factorial (Again)

(define (fact n)
  (if (= n 0)
      1
      (* n (fact (- n 1)))))

(define (fact-tail n)
  (define (helper n prod)
    (if (= n 0)
        prod
        (helper (- n 1) (* n prod))))
  (helper n 1))

;; (fact 10)
;; (fact 1000)
;; (fact-tail 10)
;; (fact-tail 1000)


;; Example: Length

(define (length s)
  (if (null? s) 0
      (+ 1 (length (cdr s)))))

(define (length-tail s)
  (define (length-iter s n)
    (if (null? s) n
        (length-iter (cdr s) (+ 1 n))))
  (length-iter s 0))


;;; Streams

(car (cons-stream 1 2))
; expect 1

(cdr-stream (cons-stream 1 2))
; expect 2

(cons-stream 1 (cons-stream 2 nil))

(cons-stream 1 (/ 1 0))

(car (cons-stream 1 (/ 1 0)))
; expect 1

; (cdr-stream (cons-stream 1 (/ 1 0)))
; expect Error


;; Infinite Streams

(define (take stream k)
  (if (= k 0)
      nil
      (cons (car stream) (take (cdr-stream stream) (- k 1)))))

(define (int-stream start)
  (cons-stream
   start
   (int-stream (+ start 1))))

(define ones (cons-stream 1 ones))

(define (add-streams s1 s2)
  (cons-stream
   (+ (car s1) (car s2))
   (add-streams
    (cdr-stream s1)
    (cdr-stream s2))))

(define ints
  (cons-stream
   1
   (add-streams ones ints)))

;; Sieve of Primes

(define (filter-stream f stream)
  (if (f (car stream))
      (cons-stream (car stream)
                   (filter-stream f
                                  (cdr-stream stream)))
      (filter-stream f (cdr-stream stream))))

(define (sieve s)
  (cons-stream
   (car s)
   (sieve (filter-stream
           (lambda (x) (> (modulo x (car s)) 0))
           (cdr-stream s)))))

(define primes (sieve (int-stream 2)))

;;; Symbolic Programming

(define (cadr s)  (car (cdr s)))
(define (cddr s)  (cdr (cdr s)))
(define (caddr s) (car (cdr (cdr s))))


(define (map f s)
  (if (null? s)
      nil
      (cons (f (car s)) (map f (cdr s)))))

(define (filter f s)
  (cond ((null? s) nil)
        ((f (car s)) (cons (car s)
                              (filter f (cdr s))))
        (else (filter f (cdr s)))))

;; List Comprehensions in Scheme

;; ((* x x) for x in '(1 2 3 4) if (> x 2)) -> (9 16)
;; (<map-exp> for <name> in <seq> if <filter-exp>)
;; (map (lambda (<name>) <map-exp>)
;;      (filter (lambda (<name>) <filter-exp>)
;;              seq))

(define (list-comp exp)
  (let ((map-exp (car exp))
        (name (car (cddr exp)))
        (seq (car (cddr (cddr exp))))
        (filter-exp (car (cddr (cddr (cddr exp))))))
    (let ((map-fn (list 'lambda (list name) map-exp))
          (filter-fn (list 'lambda (list name) filter-exp)))
      (list 'map map-fn (list 'filter filter-fn seq)))))

(define exp0 '((* x x) for x in '(1 2 3 4) if (> x 2)))
(list-comp '((* x x) for x in '(1 2 3 4) if (> x 2)))
; (map (lambda (x) (* x x)) (filter (lambda (x) (> x 2)) '(1 2 3 4)))
(eval (list-comp '((* x x) for x in '(1 2 3 4) if (> x 2))))
; (9 16)

;; Rational Numbers

(define (rats exp)
  (let ((op (car exp))
        (n1 (cadr  (cadr exp)))
        (d1 (caddr (cadr exp)))
        (n2 (cadr  (caddr exp)))
        (d2 (caddr (caddr exp))))
    ;; (print op)
    ;; (print n1)
    ;; (print d1)
    ;; (print n2)
    ;; (print d2)
    ((cond ((or (equal? op '+) (equal? op '-)) add-sub-rats)
           ((equal? op '*) mul-rats)
           (else div-rats))
     op n1 d1 n2 d2)))
            
(define (add-sub-rats op n1 d1 n2 d2)
  (list '/
        (list op
              (list '* n1 d2)
              (list '* n2 d1))
        (list '* d1 d2)))

(define (mul-rats op n1 d1 n2 d2)
  (list '/
        (list op n1 n2)
        (list op d1 d2)))

(define (div-rats op n1 d1 n2 d2)
  (mul-rats '* n1 d1 d2 n2))

(define exp1 '(+ (/ 1 10) (/ 2 10)))
(define exp2 '(* (/ 1 10) (/ 2 10)))
(define exp3 '(/ (/ 1 10) (/ 3 10)))

(eval '(+ (/ 1 10) (/ 2 10)))
; expect 0.30000000000000004
(eval (rats '(+ (/ 1 10) (/ 2 10))))
; expect 0.3
(eval '(* (/ 1 10) (/ 2 10)))
; expect 0.020000000000000004
(eval (rats '(* (/ 1 10) (/ 2 10))))
; expect 0.02
(eval '(/ (/ 1 10) (/ 3 10)))
; expect 0.33333333333333337
(eval (rats '(/ (/ 1 10) (/ 3 10))))
; expect 0.3333333333333333

(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.
(define (map proc items)
  (if (eq? items nil) nil
     (cons (proc (car items)) (map proc (cdr items)))
  )
)

(define (cons-all first rests)
  (if (eq? rests nil) nil
    (
     cons (cons first (car rests)) (cons-all first (cdr rests))
    )))

(define (zip pairs)
  (if (eq? pairs nil) '(()())
    (list (cons (caar pairs) (car (zip (cdr pairs))) )
          (cons (car (cdar pairs)) (car (cdr (zip (cdr pairs)))) )
    )
  )  
)

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  (define (helper s i) 
    (if (eq? s nil) nil
      (cons (list i (car s)) (helper (cdr s) (+ i 1)))
  ))
  (helper s 0)
  )
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 18
  (cond (  (< total 0) nil  )
        (  (= total 0) '(())  )
        (  (eq? denoms nil) nil  )
        (  else
          (if (not (eq? nil (list-change (- total (car denoms)) denoms)))
              (append 
                (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) 
                (list-change total (cdr denoms)) )
              ( list-change total (cdr denoms) )              
          )
        )
  )
)
  ; END PROBLEM 18t 

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (append (list form params) (map let-to-lambda body))
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (append  (list ( append (list 'lambda (car (zip values))) (map let-to-lambda body)) )   (map let-to-lambda (cadr (zip values)))  )
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))

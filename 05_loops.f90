program loops

    implicit none

    integer :: n, i

    read *, n
    do i = 1, 10
        print '(i0," x ",i0," = ",i0)', n, i, n*i
    end do
    
end program loops
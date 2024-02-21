program main
    integer :: n
    read *, n
    if (mod(n, 2) /= 0 .or. (6 <= n .and. n <=20)) then
        print '(a)', "Weird"
    else
        print '(a)', "Not Weird"
    end if 
end program main
#!/usr/bin/ruby

# Ruby version of my Python "ps.py"
# This programs run a shell cmd which is "ps auxww" 
# then print the result if PID > 200 and cmd begins with "/"

cmd = `ps auxww`

for line in cmd
    a = line.split()

    if a[1] == 'PID'
        print line
    elsif a[1].to_i > 200
        if a[10] =~ /^\//
            print line
        end
    end
end

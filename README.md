# get_size
get the size of a directory in python

You can create an alias in your bashrc/zshrc or cp the file into somewhere on your path (for instance $HOME/bin/), add the shebang line, and make the file executable:
<br>
```
rxlx ~ $ head $HOME/bin/get-size 
#!/usr/bin/env python3    #<--example shebang line
(code truncated for brevity)

rxlx ~ $ which get-size 
/home/rxlx/bin/get-size
rxlx ~ $ get-size $HOME/bin/
skipping symbolic link: /home/rxlx/bin/python
found the following extensions:

 113.93 MiB         41
 339.72 KiB .txt    48
 207.81 KiB .py     102
   2.46 KiB .sh     7
  12.00 KiB .swp    1
   8.21 KiB .pyc    5
 196.10 KiB .zip    3
   1.22 MiB .log    5
 596.00   B .yml    1
 394.00   B .exp    6
  55.00   B .com    1
 907.00   B .rex    3
  44.00   B .link   1
 576.00   B .dconf  1
  68.00   B .stuff  2
 332.00   B .notes  1
   1.10 KiB .xml    1
found 229 files totaling  110.67 MiB in size
rxlx ~ $
```

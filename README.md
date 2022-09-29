# iprint
Inline attributes for printing. or html style attributes


## Getting Started

```bash

git clone https://github.com/Donny-GUI/iprint.git


```

## importing module

```python
from iprint import iprint, inline

iprint("<bold green on blue> Hello world in color! </bold green on blue>")
inline("<bold green on blue> Hello world in color! </bold green on blue>")

iprint_examples()
iprint_display()

```

## tag syntax
```
<style if any> <text color> on <background color>
```
or 
```
<text color>
```
or 
```
bg<color>
```
## Available Tags

```
black
red
green
yellow
blue
magenta
cyan
white
bgblack
bgred
bggreen
bgyellow
bgblue
bgmagenta
bgcyan
bgwhite
black on black                  
bold black on black             
dim black on black              
italic black on black           
underline black on black        
blink black on black            
doubleblink black on black      
crossout black on black         
black on red                    
bold black on red               
dim black on red                
italic black on red             
underline black on red          
blink black on red              
doubleblink black on red        
crossout black on red           
black on green                  
bold black on green             
dim black on green              
italic black on green           
underline black on green        
blink black on green            
doubleblink black on green      
crossout black on green         
black on yellow                 
bold black on yellow            
dim black on yellow             
italic black on yellow          
underline black on yellow       
blink black on yellow           
doubleblink black on yellow     
crossout black on yellow        
black on blue                   
bold black on blue              
dim black on blue               
italic black on blue            
underline black on blue         
blink black on blue             
doubleblink black on blue       
crossout black on blue          
black on magenta                
bold black on magenta           
dim black on magenta            
italic black on magenta         
underline black on magenta      
blink black on magenta          
doubleblink black on magenta    
crossout black on magenta       
black on cyan                   
bold black on cyan              
dim black on cyan               
italic black on cyan            
underline black on cyan         
blink black on cyan             
doubleblink black on cyan       
crossout black on cyan          
black on white                  
bold black on white             
dim black on white              
italic black on white           
underline black on white        
blink black on white            
doubleblink black on white      
crossout black on white         
red on black                    
bold red on black               
dim red on black                
italic red on black             
underline red on black          
blink red on black              
doubleblink red on black        
crossout red on black           
red on red                      
bold red on red                 
dim red on red                  
italic red on red               
underline red on red            
blink red on red                
doubleblink red on red          
crossout red on red             
red on green                    
bold red on green               
dim red on green                
italic red on green             
underline red on green          
blink red on green              
doubleblink red on green        
crossout red on green           
red on yellow                   
bold red on yellow              
dim red on yellow               
italic red on yellow            
underline red on yellow         
blink red on yellow             
doubleblink red on yellow       
crossout red on yellow          
red on blue                     
bold red on blue                
dim red on blue                 
italic red on blue              
underline red on blue           
blink red on blue               
doubleblink red on blue         
crossout red on blue            
red on magenta                  
bold red on magenta             
dim red on magenta              
italic red on magenta           
underline red on magenta        
blink red on magenta            
doubleblink red on magenta      
crossout red on magenta         
red on cyan                     
bold red on cyan                
dim red on cyan                 
italic red on cyan              
underline red on cyan           
blink red on cyan               
doubleblink red on cyan         
crossout red on cyan            
red on white                    
bold red on white               
dim red on white                
italic red on white             
underline red on white          
blink red on white              
doubleblink red on white        
crossout red on white           
green on black                  
bold green on black             
dim green on black              
italic green on black           
underline green on black        
blink green on black            
doubleblink green on black      
crossout green on black         
green on red                    
bold green on red               
dim green on red                
italic green on red             
underline green on red          
blink green on red              
doubleblink green on red        
crossout green on red           
green on green                  
bold green on green             
dim green on green              
italic green on green           
underline green on green        
blink green on green            
doubleblink green on green      
crossout green on green         
green on yellow                 
bold green on yellow            
dim green on yellow             
italic green on yellow          
underline green on yellow       
blink green on yellow           
doubleblink green on yellow     
crossout green on yellow        
green on blue                   
bold green on blue              
dim green on blue               
italic green on blue            
underline green on blue         
blink green on blue             
doubleblink green on blue       
crossout green on blue          
green on magenta                
bold green on magenta           
dim green on magenta            
italic green on magenta         
underline green on magenta      
blink green on magenta          
doubleblink green on magenta    
crossout green on magenta       
green on cyan                   
bold green on cyan              
dim green on cyan               
italic green on cyan            
underline green on cyan         
blink green on cyan             
doubleblink green on cyan       
crossout green on cyan          
green on white                  
bold green on white             
dim green on white              
italic green on white           
underline green on white        
blink green on white            
doubleblink green on white      
crossout green on white         
yellow on black                 
bold yellow on black            
dim yellow on black             
italic yellow on black          
underline yellow on black       
blink yellow on black           
doubleblink yellow on black     
crossout yellow on black        
yellow on red                   
bold yellow on red              
dim yellow on red               
italic yellow on red            
underline yellow on red         
blink yellow on red             
doubleblink yellow on red       
crossout yellow on red          
yellow on green                 
bold yellow on green            
dim yellow on green             
italic yellow on green          
underline yellow on green       
blink yellow on green           
doubleblink yellow on green     
crossout yellow on green        
yellow on yellow                
bold yellow on yellow           
dim yellow on yellow            
italic yellow on yellow         
underline yellow on yellow      
blink yellow on yellow          
doubleblink yellow on yellow    
crossout yellow on yellow       
yellow on blue                  
bold yellow on blue             
dim yellow on blue              
italic yellow on blue           
underline yellow on blue        
blink yellow on blue            
doubleblink yellow on blue      
crossout yellow on blue         
yellow on magenta               
bold yellow on magenta          
dim yellow on magenta           
italic yellow on magenta        
underline yellow on magenta     
blink yellow on magenta         
doubleblink yellow on magenta   
crossout yellow on magenta      
yellow on cyan                  
bold yellow on cyan             
dim yellow on cyan              
italic yellow on cyan           
underline yellow on cyan        
blink yellow on cyan            
doubleblink yellow on cyan      
crossout yellow on cyan         
yellow on white                 
bold yellow on white            
dim yellow on white             
italic yellow on white          
underline yellow on white       
blink yellow on white           
doubleblink yellow on white     
crossout yellow on white        
blue on black                   
bold blue on black              
dim blue on black               
italic blue on black            
underline blue on black         
blink blue on black             
doubleblink blue on black       
crossout blue on black          
blue on red                     
bold blue on red                
dim blue on red                 
italic blue on red              
underline blue on red           
blink blue on red               
doubleblink blue on red         
crossout blue on red            
blue on green                   
bold blue on green              
dim blue on green               
italic blue on green            
underline blue on green         
blink blue on green             
doubleblink blue on green       
crossout blue on green          
blue on yellow                  
bold blue on yellow             
dim blue on yellow              
italic blue on yellow           
underline blue on yellow        
blink blue on yellow            
doubleblink blue on yellow      
crossout blue on yellow         
blue on blue                    
bold blue on blue               
dim blue on blue                
italic blue on blue             
underline blue on blue          
blink blue on blue              
doubleblink blue on blue        
crossout blue on blue           
blue on magenta                 
bold blue on magenta            
dim blue on magenta             
italic blue on magenta          
underline blue on magenta       
blink blue on magenta           
doubleblink blue on magenta     
crossout blue on magenta        
blue on cyan                    
bold blue on cyan               
dim blue on cyan                
italic blue on cyan             
underline blue on cyan          
blink blue on cyan              
doubleblink blue on cyan        
crossout blue on cyan           
blue on white                   
bold blue on white              
dim blue on white               
italic blue on white            
underline blue on white         
blink blue on white             
doubleblink blue on white       
crossout blue on white          
magenta on black                
bold magenta on black           
dim magenta on black            
italic magenta on black         
underline magenta on black      
blink magenta on black          
doubleblink magenta on black    
crossout magenta on black       
magenta on red                  
bold magenta on red             
dim magenta on red              
italic magenta on red           
underline magenta on red        
blink magenta on red            
doubleblink magenta on red      
crossout magenta on red         
magenta on green                
bold magenta on green           
dim magenta on green            
italic magenta on green         
underline magenta on green      
blink magenta on green          
doubleblink magenta on green    
crossout magenta on green       
magenta on yellow               
bold magenta on yellow          
dim magenta on yellow           
italic magenta on yellow        
underline magenta on yellow     
blink magenta on yellow         
doubleblink magenta on yellow   
crossout magenta on yellow      
magenta on blue                 
bold magenta on blue            
dim magenta on blue             
italic magenta on blue          
underline magenta on blue       
blink magenta on blue           
doubleblink magenta on blue     
crossout magenta on blue        
magenta on magenta              
bold magenta on magenta         
dim magenta on magenta          
italic magenta on magenta       
underline magenta on magenta    
blink magenta on magenta        
doubleblink magenta on magenta  
crossout magenta on magenta     
magenta on cyan                 
bold magenta on cyan            
dim magenta on cyan             
italic magenta on cyan          
underline magenta on cyan       
blink magenta on cyan           
doubleblink magenta on cyan     
crossout magenta on cyan        
magenta on white                
bold magenta on white           
dim magenta on white            
italic magenta on white         
underline magenta on white      
blink magenta on white          
doubleblink magenta on white    
crossout magenta on white       
cyan on black                   
bold cyan on black              
dim cyan on black               
italic cyan on black            
underline cyan on black         
blink cyan on black             
doubleblink cyan on black       
crossout cyan on black          
cyan on red                     
bold cyan on red                
dim cyan on red                 
italic cyan on red              
underline cyan on red           
blink cyan on red               
doubleblink cyan on red         
crossout cyan on red            
cyan on green                   
bold cyan on green              
dim cyan on green               
italic cyan on green            
underline cyan on green         
blink cyan on green             
doubleblink cyan on green       
crossout cyan on green          
cyan on yellow                  
bold cyan on yellow             
dim cyan on yellow              
italic cyan on yellow           
underline cyan on yellow        
blink cyan on yellow            
doubleblink cyan on yellow      
crossout cyan on yellow         
cyan on blue                    
bold cyan on blue               
dim cyan on blue                
italic cyan on blue             
underline cyan on blue          
blink cyan on blue              
doubleblink cyan on blue        
crossout cyan on blue           
cyan on magenta                 
bold cyan on magenta            
dim cyan on magenta             
italic cyan on magenta          
underline cyan on magenta       
blink cyan on magenta           
doubleblink cyan on magenta     
crossout cyan on magenta        
cyan on cyan                    
bold cyan on cyan               
dim cyan on cyan                
italic cyan on cyan             
underline cyan on cyan          
blink cyan on cyan              
doubleblink cyan on cyan        
crossout cyan on cyan           
cyan on white                   
bold cyan on white              
dim cyan on white               
italic cyan on white            
underline cyan on white         
blink cyan on white             
doubleblink cyan on white       
crossout cyan on white          
white on black                  
bold white on black             
dim white on black              
italic white on black           
underline white on black        
blink white on black            
doubleblink white on black      
crossout white on black         
white on red                    
bold white on red               
dim white on red                
italic white on red             
underline white on red          
blink white on red              
doubleblink white on red        
crossout white on red           
white on green                  
bold white on green             
dim white on green              
italic white on green           
underline white on green        
blink white on green            
doubleblink white on green      
crossout white on green         
white on yellow                 
bold white on yellow            
dim white on yellow             
italic white on yellow          
underline white on yellow       
blink white on yellow           
doubleblink white on yellow     
crossout white on yellow        
white on blue                   
bold white on blue              
dim white on blue               
italic white on blue            
underline white on blue         
blink white on blue             
doubleblink white on blue       
crossout white on blue          
white on magenta                
bold white on magenta           
dim white on magenta            
italic white on magenta         
underline white on magenta      
blink white on magenta          
doubleblink white on magenta    
crossout white on magenta       
white on cyan                   
bold white on cyan              
dim white on cyan               
italic white on cyan            
underline white on cyan         
blink white on cyan             
doubleblink white on cyan       
crossout white on cyan          
white on white                  
bold white on white             
dim white on white              
italic white on white           
underline white on white        
blink white on white            
doubleblink white on white      
crossout white on white         
bold black                      
bold red                        
bold green                      
bold yellow                     
bold blue                       
bold magenta                    
bold cyan                       
bold white                      
dim black                       
dim red                         
dim green                       
dim yellow                      
dim blue                        
dim magenta                     
dim cyan                        
dim white                       
italic black                    
italic red                      
italic green                    
italic yellow                   
italic blue                     
italic magenta                  
italic cyan                     
italic white                    
underline black                 
underline red                   
underline green                 
underline yellow                
underline blue                  
underline magenta               
underline cyan                  
underline white                 
blink black                     
blink red                       
blink green                     
blink yellow                    
blink blue                      
blink magenta                   
blink cyan                      
blink white                     
doubleblink black               
doubleblink red                 
doubleblink green               
doubleblink yellow              
doubleblink blue                
doubleblink magenta             
doubleblink cyan                
doubleblink white               
crossout black                  
crossout red                    
crossout green                  
crossout yellow                 
crossout blue                   
crossout magenta                
crossout cyan                   
crossout white                  
```

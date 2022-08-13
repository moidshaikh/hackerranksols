<div class="markdown -arial"><p>You have a hierarchy of directories and some files in some of those directories:</p>
<pre><code>/root/devops/dir1/file1.txt, file2.txt, ... 
/root/devops/dir2/file3.txt, file4, ...
/root/devops/file6.in, file7.out, ...
...
</code></pre>
<p>Some of these files contain <strong>IP addresses</strong> inside the text. An <strong>IP address</strong> is a string of form <code>x.x.x.x</code> where each <code>x</code> is a number from <code>0</code> to <code>255</code> (inclusive).</p>
<p>For example, say we have <code>file1.txt</code> that looks like this:</p>
<pre><code>hello world 127.0.0.1 
this is some example 128.99.107.55 
file with some correct and incorrect 128.128.4.11 ip 0.11.1115.78 addresses
</code></pre>
<p>This file contains only 3 IP addresses, namely <code>127.0.0.1</code>, <code>128.99.107.55</code>, and <code>128.128.4.11</code>, since <code>0.11.1115.78</code> is not a valid IP address.</p>
<p>Your task is to find all <strong>distinct IP addresses</strong> from all the files in the <strong>/root/devops/</strong> directory and print them in <a href="keyword://lexicographical-order-for-strings" target="_blank">lexicographical order</a>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For the following <code>/root/devops/</code> directory:</p>
<p><strong>/root/devops/dir1/file1.txt</strong></p>
<pre><code>    hello world 127.0.0.1 
    this is some example 128.99.107.55 
    file with some correct and incorrect 128.128.4.11 ip 0.11.1115.78 addressesaddresses
</code></pre>
<p><strong>/root/devops/dir1/file2.txt</strong></p>
<pre><code>    hello from 74.0.65.76 and 8.dd.99.88.907 good
    this is some example 306.5.76.35 
    file with some correct and incorrect 15.128.4.65 ip addresses
    0.0.0.0
</code></pre>
<p><strong>/root/devops/dir2/file3.txt</strong></p>
<pre><code>    127.65.64.1 127.0.64.1 127.0.0.1
    exaMple 128.57.107.76 128.57.907.70 
    file with some correct and incorrect 67.128.4.11 ip addresses 7.7.7.8
</code></pre>
<p><strong>/root/devops/dir2/file4.txt</strong></p>
<pre><code>    hello world 127.98.0.1 
    this is some example 128.96.107.55 
    file with some correct and incorrect 128.68.4.11 ip addresses
</code></pre>
<p><strong>/root/devops/f.inp</strong></p>
<pre><code>    hello world 127.0.49.1 
    this is some example 128.99.58.55 8.88.888.88 77.255.255.254
    7.7.257.25 file with some correct and incorrect 26.56.4.23 ip addresses
</code></pre>
<p>the output should be</p>
<pre><code>0.0.0.0
127.0.0.1
127.0.49.1
127.0.64.1
127.65.64.1
127.98.0.1
128.128.4.11
128.57.107.76
128.68.4.11
128.96.107.55
128.99.107.55
128.99.58.55
15.128.4.65
26.56.4.23
67.128.4.11
7.7.7.8
74.0.65.76
77.255.255.254
</code></pre>
<ul>
<li><strong>[execution time limit] 8 seconds (py3)</strong></li>
</ul>
</div>
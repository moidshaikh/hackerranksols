<div class="markdown -arial"><p>There is a common versioning practice in software management world - “Semantic Versioning”. Consider a version format of <code>X.Y.Z</code> (Major.Minor.Patch). Bug fixes not affecting the API increment the patch version, backwards compatible API additions/changes increment the minor version, and backwards incompatible API changes increment the major version. Under this scheme, version numbers and the way they change convey meaning about the underlying code and what has been modified from one version to the next.</p>
<p>In this task you will be given a git repository located at <code>/root/devops/someRepo</code>, you need to:</p>
<ol>
<li>Find out its current version based on the latest git tag.</li>
<li>Then you should determine if the last update is a major, a minor, or a patch update. You can determine it by querying to an API with url <code>http://localhost:8888/update</code>.  A GET request to that url will retrieve  <code>"patch"</code>, <code>"minor"</code> or <code>"major"</code>.</li>
<li>Modify the <code>deploy.yml</code> file with the new version. The value <code>latestImage</code> should be updated.</li>
<li>Finally you should create a new git lightweight tag based on the new version.</li>
</ol>
<p>The final output of your program should be the new <code>deploy.yml</code> file and the command used to create the git tag.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/semanticVersioning/img/example.png?_tm=1589878695878" alt=""></p>
<p>The content of <code>deploy.yml</code> is</p>
<pre><code>appName: myProject
latestImage: v0.0.0
services:
  webapp:
    build:
      context: ./dir
      dockerfile: Dockerfile-alternate
      args:
        buildno: 1
  microservice: www.example.com/api
</code></pre>
<p>The latest git tag is named <code>v0.1.3</code>, thus the project was subject to <em>1</em> <em>minor</em> update along with <em>3</em> followed <em>patch</em> updates. Assume the API responds <code>"minor"</code> i.e. the next update is a <em>minor</em> update. Therefore the new version should increment the <em>minor</em> version and reset the <em>patch</em> version yielding <code>v0.2.0</code>.</p>
<p>The output should contain the contents of <code>deploy.yml</code> and the git tag command.</p>
<pre><code>appName: myProject
latestImage: v0.2.0
services:
  webapp:
    build:
      context: ./dir
      dockerfile: Dockerfile-alternate
      args:
        buildno: 1
  microservice: www.example.com/api
git tag v0.2.0
</code></pre>
<ul>
<li><strong>[execution time limit] 15 seconds (py3)</strong></li>
</ul>
</div>
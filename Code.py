<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=UTF-8">
<link rel="stylesheet"
href="usr/share/git/ReleaseNotes.css">
</head>
<body class="details">
<div class="links">
<ul>
<li><a href="https://gitforwindows.org/">homepage</a></li>
<li><a href="https://github.com/git-for-windows/git/wiki/FAQ">faq</a></li>
<li><a href="https://gitforwindows.org/#contribute">contribute</a></li>
<li><a href="https://gitforwindows.org/#contribute">bugs</a></li>
<li><a href="mailto:git@vger.kernel.org">questions</a></li>
</ul>
<div id="git-for-windows-logo">
<div id="left-pane"></div>
<div id="top-pane"></div>
<div id="right-pane"></div>
<div id="bottom-pane"></div>
<div id="diagonal-pipe"></div>
<div id="vertical-pipe"></div>
<div id="top-ball"></div>
<div id="bottom-ball"></div>
<div id="right-ball"></div>
</div>
</div>
<div class="content">
<h1>Git for Windows v2.47.1(2) Release Notes</h1>

<p>Latest update: January 14th 2025</p>

<h2>Introduction</h2>

<p>These release notes describe issues specific to the Git for Windows release. The release notes covering the history of the core git commands can be found <a href="https://github.com/git/git/tree/HEAD/Documentation/RelNotes">in the Git project</a>.</p>

<p>See <a href="http://git-scm.com/">http://git-scm.com/</a> for further details about Git including ports to other operating systems. Git for Windows is hosted at <a href="https://gitforwindows.org/">https://gitforwindows.org/</a>.</p>

<h1 id="known-issues" class="collapsible">Known issues</h1>

<ul>
<li>On Windows 10 before 1703, or when Developer Mode is turned off, special permissions are required when cloning repositories with symbolic links, therefore support for symbolic links is disabled by default. Use <code>git clone -c core.symlinks=true &lt;URL&gt;</code> to enable it, see details <a href="https://github.com/git-for-windows/git/wiki/Symbolic-Links">here</a>.</li>
<li>If configured to use Plink, you will have to connect with <a href="http://www.chiark.greenend.org.uk/~sgtatham/putty/">putty</a> first and accept the host key.</li>
<li>Some console programs, most notably non-MSYS2 Python, PHP, Node and OpenSSL, interact correctly with MinTTY only when called through <code>winpty</code> (e.g. the Python console needs to be started as <code>winpty python</code> instead of just <code>python</code>).</li>
<li><p>If you specify command-line options starting with a slash, POSIX-to-Windows path conversion will kick in converting e.g. "<code>/usr/bin/bash.exe</code>" to "<code>C:\Program Files\Git\usr\bin\bash.exe</code>". When that is not desired -- e.g. "<code>--upload-pack=/opt/git/bin/git-upload-pack</code>" or "<code>-L/regex/</code>" -- you need to set the environment variable <code>MSYS_NO_PATHCONV</code> temporarily, like so:</p>

<blockquote>
  <p><code>MSYS_NO_PATHCONV=1 git blame -L/pathconv/ msys2_path_conv.cc</code></p>
</blockquote>

<p>Alternatively, you can double the first slash to avoid POSIX-to-Windows path conversion, e.g. "<code>//usr/bin/bash.exe</code>".</p></li>
<li>Windows drives are normally recognized within the POSIX path as <code>/c/path/to/dir/</code> where <code>/c/</code> (or appropriate drive letter) is equivalent to the <code>C:\</code> Windows prefix to the <code>\path\to\dir</code>. If this is not recognized, revert to the <code>C:\path\to\dir</code> Windows style.</li>
<li>Git for Windows will not allow commits containing DOS-style truncated 8.3-format filenames ending with a tilde and digit, such as <code>mydocu~1.txt</code>. A workaround is to call <code>git config core.protectNTFS false</code>, which is not advised. Instead, add a rule to .gitignore to ignore the file(s), or rename the file(s).</li>
<li>Many Windows programs (including the Windows Explorer) have problems with directory trees nested so deeply that the absolute path is longer than 260 characters. Therefore, Git for Windows refuses to check out such files by default. You can overrule this default by setting <code>core.longPaths</code>, e.g. <code>git clone -c core.longPaths=true ...</code>.</li>
<li>Some commands are not yet supported on Windows and excluded from the installation.</li>
<li>As Git for Windows is shipped without Python support, <code>git p4</code> (which is backed by a Python script) is not supported.</li>
<li>The Quick Launch icon will only be installed for the user running setup (typically the Administrator). This is a technical restriction and will not change.</li>
<li>Git command hints are designed for a POSIX shell, this can lead to issues when using them <strong>as is</strong> in non-POSIX shells like PowerShell, <a href="https://github.com/git-for-windows/git/issues/2785">as is the case in this ticket</a>.</li>
<li>When pushing via the <code>git://</code> protocol, Git for Windows may hang indefinitely. The last console output in this case is typically <code>Writing objects: 100%</code>. As a workaround, disabling side-band via <code>git config sendpack.sideband false</code> should address this, at the cost of showing remote errors late (or not at all). No one is working on this; for more details, or to contribute a fix, see issue <a href="https://github.com/git-for-windows/git/issues/907">#907</a> (closed unless/until there is activity).</li>
<li><p>Git for Windows executables linked to <code>msys-2.0.dll</code> are not compatible with Mandatory ASLR and may crash if system-wide Mandatory ASLR is enabled in Windows Exploit protection. A workaround is to disable ASLR for all executables in <code>C:\Program Files\Git\usr\bin</code>, run in administrator powershell (replace <code>$_.Name</code> with <code>$_</code> to use full path to executable instead of name):</p>

<blockquote>
  <p><code>Get-Item -Path "C:\Program Files\Git\usr\bin\*.exe" | %{ Set-ProcessMitigation -Name $_.Name -Disable ForceRelocateImages }</code></p>
</blockquote>

<p>Alternatively, you can disable Mandatory ASLR completely in Windows Exploit protection.</p></li>
</ul>

<p>Should you encounter other problems, please first search <a href="https://github.com/git-for-windows/git/issues">the bug tracker</a> (also look at the closed issues) and <a href="http://groups.google.com/group/git-for-windows">the mailing list</a>, chances are that the problem was reported already. Also make sure that you use an up to date Git for Windows version (or a <a href="https://wingit.blob.core.windows.net/files/index.html">current snapshot build</a>). If it has not been reported yet, please follow <a href="https://github.com/git-for-windows/git/wiki/Issue-reporting-guidelines">our bug reporting guidelines</a> and <a href="https://github.com/git-for-windows/git/issues/new">report the bug</a>.</p>

<h2 id="licenses" class="collapsible">Licenses</h2><div>

<p>Git is licensed under the GNU General Public License version 2.</p>

<p>Git for Windows also contains Embedded CAcert Root Certificates. For more information please go to <a href="https://www.cacert.org/policy/RootDistributionLicense.php">https://www.cacert.org/policy/RootDistributionLicense.php</a>.</p>

<p>Git for Windows is distributed with other components yet, such as Bash, zlib, curl, tcl/tk, perl, MSYS2. Each of these components is governed by their respective license.</p>

</div><h2 id="v2.47.1(2)" nr="1" class="collapsible"> <a name="latest">Changes in v2.47.1(2)</a><br /><small>since  v2.47.1 (November 25th 2024)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git-ecosystem/git-credential-manager/releases/tag/v2.6.1">Git Credential Manager v2.6.1</a>, addressing CVE-2024-50338.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v3.6.1">Git LFS v3.6.1</a>, addressing CVE-2024-53263.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li><a href="https://github.com/git-ecosystem/git-credential-manager/security/advisories/GHSA-86c2-4x57-wc8g"><strong>CVE-2024-50338</strong></a>: Git Credential Manager can be tricked to exfiltrate credentials for a trusted site to an untrusted site. Since the URLs needed for such an attack look suspicious, this usually requires a recursive clone or fetch.</li>
<li><a href="https://github.com/git-lfs/git-lfs/security/advisories/GHSA-q6r2-x2cc-vrp7"><strong>CVE-2024-53263</strong></a>: In conjunction with CVE-2024-52006, Git LFS can be tricked to exfiltrate credentials for a trusted site to an untrusted site.</li>
<li><a href="https://github.com/git/git/security/advisories/GHSA-hmg8-h7qf-7cxr"><strong>CVE-2024-50349</strong></a>: When prompting the user for a password in the terminal, Git does not neutralize control characters.</li>
<li><a href="https://github.com/git/git/security/advisories/GHSA-7jjc-gg6m-3329"><strong>CVE-2024-52005</strong></a>: The sideband channel does not neutralize control characters.</li>
<li><a href="https://github.com/git/git/security/advisories/GHSA-r5ph-xg7q-xfrp"><strong>CVE-2024-52006</strong></a>: Similar to CVE-2020-5260, affecting credential helpers that interpret Carriage Returns as newlines.</li>
</ul>

</div><h2 id="v2.47.1" nr="2" class="collapsible"> Changes in v2.47.1<br /><small>since  v2.47.0(2) (October 22nd 2024)</h2></small><div>

<p>This release comes with the first early native <a href="https://github.com/git-for-windows/git/issues/3107">support of Windows/ARM64</a>, ready for testing. Please report any issues!</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.47.1/Documentation/RelNotes/2.47.1.txt">Git v2.47.1</a>.</li>
<li>Comes with <a href="https://curl.se/changes.html#8_11_0">cURL v8.11.0</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/3.6.0">Git LFS v3.6.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Due to a bug introduced in the v2.47 cycle, <a href="https://github.com/git-for-windows/git/issues/5231">the installer showed an empty "experimental options" page</a>, which was <a href="https://github.com/git-for-windows/build-extra/pull/578">fixed</a>.</li>
<li>A potential crash in Git Bash on Insider versions of Windows/ARM64 <a href="https://github.com/git-for-windows/msys2-runtime/pull/76">was fixed</a>.</li>
<li>On Windows/ARM64, running the 64-bit version of Git for Windows could infrequently cause deadlocked threads (see e.g. <a href="https://github.com/msys2/msys2-autobuild/issues/62">this report</a> or <a href="https://inbox.sourceware.org/cygwin-developers/78f294de-4c94-242a-722e-fd98e51edff9@jdrake.com/">this one</a>), <a href="https://github.com/git-for-windows/msys2-runtime/pull/73">which was addressed</a>.</li>
</ul>

</div><h2 id="v2.47.0(2)" nr="3" class="collapsible"> Changes in v2.47.0(2)<br /><small>since  v2.47.0 (October 8th 2024)</h2></small><div>

<p>As of this version, wildcards in the command-line arguments of any <code>git.exe</code> process <a href="https://www.msys2.org/news/#2024-11-03-disabling-mingw-w64-wildcard-support-by-default">will no longer be expanded</a> (this does <em>not</em> affect wildcard expansion when calling <code>git</code> from Git Bash).</p>

<h3>Bug Fixes</h3>

<ul>
<li>A regression in v2.47.0 where <code>git maintenance start</code> crashed immediately <a href="https://github.com/git-for-windows/git/pull/5198">was fixed</a>.</li>
<li>A <a href="https://github.com/git-for-windows/git/issues/5199">regression</a> where clones, fetches and pushes via SSH would dead-lock was fixed.</li>
<li>As of Git for Windows v2.47.0, <a href="https://git-scm.com/docs/scalar">Scalar</a> was supposed to enable <a href="https://github.com/git-for-windows/git/pull/5171">an optimized push algorithm</a>, but for a typo didn't, which <a href="https://github.com/git-for-windows/git/pull/5220">was fixed</a>.</li>
<li>A few documentation and other, minor bug fixes from upstream Git <a href="https://github.com/git-for-windows/git/pull/5221">were integrated into Git for Windows early</a>.</li>
</ul>

</div><h2 id="v2.47.0" nr="4" class="collapsible"> Changes in v2.47.0<br /><small>since  v2.46.2 (September 24th 2024)</h2></small><div>

<p>Git for Windows for Windows v2.47 drops support for Windows 7 and for Windows 8, as announced previously.</p>

<p>Please also note that the 32-bit variant of Git for Windows is deprecated; Its last official release <a href="https://gitforwindows.org/32-bit.html">is planned for 2025</a>.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.47.0/Documentation/RelNotes/2.47.0.txt">Git v2.47.0</a>.</li>
<li>Comes with the MSYS2 runtime (Git for Windows flavor) based on <a href="https://inbox.sourceware.org/cygwin-announce/20240825195526.2571058-1-corinna-cygwin@cygwin.de/">Cygwin v3.5.4</a>, which drops Windows 7 and Windows 8 support.</li>
<li>The new, experimental <code>git backfill</code> command <a href="https://github.com/git-for-windows/git/pull/5172">was added</a>: It helps fetching relevant Git objects smartly in a partial, sparse clone.</li>
<li>The new, experimental <a href="https://github.com/git-for-windows/git/pull/5174"><code>git survey</code> command was added</a>. This command is designed to help identify less-than-ideal data shape in monorepos, and it will likely see highly active development. Stay tuned!</li>
<li>Comes with <a href="https://github.com/git-ecosystem/git-credential-manager/releases/tag/v2.6.0">Git Credential Manager v2.6.0</a>.</li>
</ul>

</div><h2 id="v2.46.2" nr="5" class="collapsible"> Changes in v2.46.2<br /><small>since  v2.46.1 (September 18th 2024)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.46.2/Documentation/RelNotes/2.46.2.txt">Git v2.46.2</a>.</li>
<li>Comes with <a href="https://github.com/openssh/openssh-portable/releases/tag/V_9_9_P1">OpenSSH v9.9.P1</a>.</li>
<li>Comes with <a href="https://github.com/mintty/mintty/releases/tag/3.7.6">MinTTY v3.7.6</a>.</li>
<li>Comes with <a href="https://git.savannah.gnu.org/cgit/bash.git/commit/?id=6794b5478f660256a1023712b5fc169196ed0a22">Bash v5.2.37</a>.</li>
<li>Comes with the <a href="https://github.com/git-for-windows/git/pull/5157">new, experimental <code>--full-name-hash</code> option for <code>git repack</code></a> that helps packing monorepos more tightly.</li>
</ul>

</div><h2 id="v2.46.1" nr="6" class="collapsible"> Changes in v2.46.1<br /><small>since  v2.46.0 (July 29th 2024)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.46.1/Documentation/RelNotes/2.46.1.txt">Git v2.46.1</a>.</li>
<li>Comes with <a href="https://git.savannah.gnu.org/cgit/bash.git/commit/?id=142bbdd89e4d5bb62aea4469d1d2c24cf470afd8">Bash v5.2.32</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-3.2-notes.html">OpenSSL v3.2.3</a>.</li>
<li>Comes with <a href="https://github.com/mintty/mintty/releases/tag/3.7.5">MinTTY v3.7.5</a>.</li>
<li>Comes with <a href="https://curl.se/changes.html#8_10_1">cURL v8.10.1</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The support code enabled via <code>core.WSLCompat</code> did not work well with files stored in subdirectories of the worktree, which <a href="https://github.com/git-for-windows/git/pull/4660">has been fixed</a>.</li>
<li>When using an <code>askpass</code> helper (e.g. implicitly when running inside VS Code's internal terminal), Git v2.46.0 <a href="https://github.com/git-for-windows/git/issues/5115">would error out with "read error: Invalid argument"</a>; This bug has been fixed.</li>
</ul>

</div><h2 id="v2.46.0" nr="7" class="collapsible"> Changes in v2.46.0<br /><small>since  v2.45.2 (June 3rd 2024)</h2></small><div>

<p>Git for Windows for Windows v2.46 is the last version to support for Windows 7 and for Windows 8, see <a href="https://www.msys2.org/docs/windows_support/">MSYS2's corresponding deprecation announcement</a> (Git for Windows relies on MSYS2 for components such as Bash and Perl).</p>

<p>Please also note that the 32-bit variant of Git for Windows is deprecated; Its last official release <a href="https://gitforwindows.org/32-bit.html">is planned for 2025</a>.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.46.0/Documentation/RelNotes/2.46.0.txt">Git v2.46.0</a>.</li>
<li>Comes with <a href="https://github.com/openssl/openssl/releases/tag/openssl-3.2.2">OpenSSL v3.2.2</a>.</li>
<li>Comes with <a href="https://github.com/PCRE2Project/pcre2/blob/pcre2-10.44/ChangeLog">PCRE2 v10.44</a>.</li>
<li>Comes with <a href="https://github.com/openssh/openssh-portable/releases/tag/V_9_8_P1">OpenSSH v9.8.P1</a>.</li>
<li>Comes with <a href="https://github.com/git-ecosystem/git-credential-manager/releases/tag/v2.5.1">Git Credential Manager v2.5.1</a>.</li>
<li>Comes with <a href="https://github.com/mintty/mintty/releases/tag/3.7.4">MinTTY v3.7.4</a>.</li>
<li><code>git config</code> <a href="https://git-scm.com/docs/git-config#FILES">respects two user-wide configs</a>: <code>.gitconfig</code> in the home directory, and <code>.config/git/config</code>. Since the latter isn't a Windows-native directory, <a href="https://github.com/git-for-windows/git/pull/5030">Git for Windows now looks for <code>Git/config</code> in the <code>AppData</code> directory</a>, unless <code>.config/git/config</code> exists. </li>
<li>The <a href="https://github.com/git-for-windows/git/discussions/3251">FSMonitor feature</a> is no longer experimental, and therefore no longer offered as installer option. Users are encouraged to enable this on a per-repository basis, via the config setting <code>core.fsmonitor=true</code> (<code>scalar clone</code> does this automatically).</li>
<li>The server-side component of OpenSSH, which had been shipped with Git for Windows for historical reasons only, is <a href="https://github.com/git-for-windows/build-extra/pull/571">now no longer distributed with it</a>.</li>
<li>Comes with <a href="https://curl.se/changes.html#8_9_0">cURL v8.9.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git Bash's <code>ls</code> command <a href="https://github.com/git-for-windows/msys2-runtime/pull/69">can now be used in OneDrive-managed folders</a> without having to hydrate all the files.</li>
<li>Git LFS v3.5.x and newer no longer support Windows 7. Instead of a helpful error message, it now simply <a href="https://github.com/git-for-windows/git/issues/4996">crashes</a> on that Windows version, leaving the user with the error message "panic before malloc heap initialized". This has been <a href="https://github.com/git-for-windows/git/pull/5042">addressed</a>: In addition to the unhelpful error message, Git is now saying what is going on and how to get out of the situation.</li>
<li>As of v2.45.0, the manual pages of <code>git clone</code> and <code>git init</code> <a href="https://github.com/git-for-windows/git/issues/5063">were broken</a>, which has been fixed. </li>
</ul>

</div><h2 id="v2.45.2" nr="8" class="collapsible"> Changes in v2.45.2<br /><small>since  v2.45.1 (May 14th 2024)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.45.2/Documentation/RelNotes/2.45.2.txt">Git v2.45.2</a>.</li>
<li>Comes with <a href="https://github.com/jonas/tig/releases/tag/tig-2.5.10">Tig v2.5.10</a>.</li>
<li>Comes with <a href="https://github.com/curl/curl/releases/tag/curl-8_8_0">cURL v8.8.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>When Git for Windows v2.44.0 introduced the ability <a href="https://github.com/git-for-windows/git/pull/4700">to use native Win32 Console ANSI sequence processing</a>, an inadvertent fallout was that in this instance, <a href="https://github.com/git-for-windows/git/issues/4851">non-ASCII characters were no longer printed correctly unless the current code page was set to 65001</a>. This bug <a href="https://github.com/git-for-windows/git/pull/4968">has been fixed</a>.</li>
</ul>

</div><h2 id="v2.45.1" nr="9" class="collapsible"> Changes in v2.45.1<br /><small>since  v2.45.0 (April 29th 2024)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.45.1/Documentation/RelNotes/2.45.1.txt">Git v2.45.1</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li><strong>CVE-2024-32002</strong>: Recursive clones on case-insensitive filesystems that support
symbolic links are susceptible to case confusion that can be exploited to
execute just-cloned code during the clone operation.</li>
<li><strong>CVE-2024-32004</strong>: Repositories can be configured to execute arbitrary code
during local clones. To address this, the ownership checks introduced in
v2.30.3 are now extended to cover cloning local repositories.</li>
<li><strong>CVE-2024-32020</strong>: Local clones may end up hardlinking files into the target
repository's object database when source and target repository reside on the
same disk. If the source repository is owned by a different user, then those
hardlinked files may be rewritten at any point in time by the untrusted user.</li>
<li><strong>CVE-2024-32021</strong>: When cloning a local source repository that contains symlinks
via the filesystem, Git may create hardlinks to arbitrary user-readable files
on the same filesystem as the target repository in the objects/ directory.</li>
<li><strong>CVE-2024-32465</strong>: It is supposed to be safe to clone untrusted repositories,
even those unpacked from zip archives or tarballs originating from untrusted
sources, but Git can be tricked to run arbitrary code as part of the clone.</li>
<li>Defense-in-depth: submodule: require the submodule path to contain
directories only.</li>
<li>Defense-in-depth: clone: when symbolic links collide with directories, keep
the latter.</li>
<li>Defense-in-depth: clone: prevent hooks from running during a clone.</li>
<li>Defense-in-depth: core.hooksPath: add some protection while cloning.</li>
<li>Defense-in-depth: fsck: warn about symlink pointing inside a gitdir.</li>
<li>Various fix-ups on HTTP tests.</li>
<li>HTTP Header redaction code has been adjusted for a newer version of cURL
library that shows its traces differently from earlier versions.</li>
<li>Fix was added to work around a regression in libcURL 8.7.0 (which has already
been fixed in their tip of the tree).</li>
<li>Replace macos-12 used at GitHub CI with macos-13.</li>
<li>ci(linux-asan/linux-ubsan): let's save some time</li>
<li>Tests with LSan from time to time seem to emit harmless message that makes
our tests unnecessarily flakey; we work it around by filtering the
uninteresting output.</li>
<li>Update GitHub Actions jobs to avoid warnings against using deprecated version
of Node.js.</li>
</ul>

</div><h2 id="v2.45.0" nr="10" class="collapsible"> Changes in v2.45.0<br /><small>since  v2.44.0 (February 23rd 2024)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.45.0/Documentation/RelNotes/2.45.0.txt">Git v2.45.0</a>.</li>
<li>Comes with <a href="https://github.com/PCRE2Project/pcre2/releases/tag/pcre2-10.43">PCRE2 v10.43</a>.</li>
<li>Comes with <a href="https://github.com/gpg/gnupg/releases/tag/gnupg-2.4.5">GNU Privacy Guard v2.4.5</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/3.5.1">Git LFS v3.5.1</a>.</li>
<li>MinGit <a href="https://github.com/git-for-windows/build-extra/pull/550">now supports running <code>git difftool</code></a>.</li>
<li>Comes with <a href="https://github.com/openssh/openssh-portable/releases/tag/V_9_7_P1">OpenSSH v9.7.P1</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnutls-help/2024-March/004845.html">GNU TLS v3.8.4</a>.</li>
<li>Comes with <a href="https://github.com/jonas/tig/releases/tag/tig-2.5.9">Tig v2.5.9</a>.</li>
<li>Comes with <a href="https://curl.se/changes.html#8_7_1">cURL v8.7.1</a>.</li>
<li>Comes with <a href="https://github.com/git-ecosystem/git-credential-manager/releases/tag/v2.5.0">Git Credential Manager v2.5.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Since v2.14.0(2), Git for Windows' installer registers the <em>Open Git Bash here</em> and <em>Open Git GUI here</em> context menu items also in the special <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/dd758096.aspx">Libraries folders</a>, but the uninstaller never removed them from those folders, <a href="https://github.com/git-for-windows/build-extra/pull/551">which was fixed</a>.</li>
<li>A <a href="https://github.com/git-for-windows/git/issues/4843">regression</a> where <code>git clone</code> no longer worked in the presence of <code>includeIf.*.onbranch</code> config settings <a href="https://github.com/git-for-windows/git/commit/199f44cb2ead34486f2588dc32d000d17e30f9cc">has been fixed</a>.</li>
<li>Apparently some anti-malware programs fiddle with the mode of <code>stdout</code> which <a href="https://github.com/git-for-windows/git/issues/4890">can lead to problems because expected output is missing</a>, which <a href="https://github.com/git-for-windows/git/pull/4901">was fixed</a>.</li>
</ul>

</div><h2 id="v2.44.0" nr="11" class="collapsible"> Changes in v2.44.0<br /><small>since  v2.43.0 (November 20th 2023)</h2></small><div>

<p>As announced previously, Git for Windows will drop support for Windows 7 and for Windows 8 in one of the next versions, following <a href="https://www.msys2.org/docs/windows_support/">Cygwin's and MSYS2's lead</a> (Git for Windows relies on MSYS2 for components such as Bash and Perl).</p>

<p>Following the footsteps of the MSYS2 and Cygwin projects on which Git for Windows depends, the 32-bit variant of Git for Windows <a href="https://gitforwindows.org/32-bit.html">is being phased out</a>.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.44.0/Documentation/RelNotes/2.44.0.txt">Git v2.44.0</a>.</li>
<li>Comes with <a href="https://github.com/Yubico/libfido2/releases/tag/1.14.0">libfido2 v1.14.0</a>.</li>
<li>Comes with the MSYS2 runtime (Git for Windows flavor) based on <a href="https://inbox.sourceware.org/cygwin-announce/20231129150845.713029-1-corinna-cygwin@cygwin.com/">Cygwin v3.4.10</a>.</li>
<li>Comes with <a href="http://search.cpan.org/dist/perl-5.38.2/pod/perldelta.pod">Perl v5.38.2</a>.</li>
<li>Git for Windows <a href="https://github.com/git-for-windows/git/pull/4700">learned to detect and use native Windows support for ANSI sequences</a>, which allows using 24-bit colors in terminal windows.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/3.4.1">Git LFS v3.4.1</a>.</li>
<li>The repository viewer <a href="https://jonas.github.io/tig/">Tig</a> that is included in Git for Windows <a href="https://github.com/git-for-windows/MINGW-packages/pull/104">can now be called also directly from PowerShell/CMD</a>.</li>
<li>Comes with <a href="https://github.com/openssh/openssh-portable/releases/tag/V_9_6_P1">OpenSSH v9.6.P1</a>.</li>
<li>Comes with <a href="https://git.savannah.gnu.org/cgit/bash.git/commit/?id=f3b6bd19457e260b65d11f2712ec3da56cef463f">Bash v5.2.26</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnutls-help/2024-January/004841.html">GNU TLS v3.8.3</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-3.2-notes.html">OpenSSL v3.2.1</a>.</li>
<li>Comes with <a href="https://curl.se/changes.html#8_6_0">cURL v8.6.0</a>.</li>
<li>Comes with <a href="https://github.com/gpg/gnupg/releases/tag/gnupg-2.4.4">GNU Privacy Guard v2.4.4</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The 32-bit variant of Git for Windows was missing some MSYS2 runtime updates, <a href="https://github.com/git-for-windows/MSYS2-packages/pull/138">which was addressed</a>; Do note <a href="https://gitforwindows.org/32-bit.html">32-bit support is phased out</a>.</li>
<li>The Git for Windows installer <a href="https://github.com/git-for-windows/git/issues/4727">showed cut-off text in some setups</a>. This <a href="https://github.com/git-for-windows/build-extra/pull/536">has been fixed</a>.</li>
<li>The <code>git credential-manager --help</code> command previously would not find a page to display in the web browser, <a href="https://github.com/git-for-windows/build-extra/pull/542">which has been fixed</a>.</li>
<li>A couple of bugs that could cause Git Bash to hang in certain scenarios <a href="https://github.com/git-for-windows/MSYS2-packages/pull/158">were fixed</a>.</li>
</ul>

</div><h2 id="v2.43.0" nr="12" class="collapsible"> Changes in v2.43.0<br /><small>since  v2.42.0(2) (August 30th 2023)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.43.0/Documentation/RelNotes/2.43.0.txt">Git v2.43.0</a>.</li>
<li>Comes with <a href="https://github.com/cygwin/cygwin/releases/tag/cygwin-3.4.9">MSYS2 runtime v3.4.9</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnutls-help/2023-August/004834.html">GNU TLS v3.8.1</a>.</li>
<li>When installing into a Windows setup with Mandatory Address Space Layout Randomization (ASLR) enabled, which is incompatible with the MSYS2 runtime powering Git Bash, SSH and some other programs distributed with Git for Windows, <a href="https://github.com/git-for-windows/build-extra/pull/513">the Git for Windows installer now offers to add exceptions</a> that will allow those programs to work as expected.</li>
<li>Comes with <a href="https://github.com/openssh/openssh-portable/releases/tag/V_9_5_P1">OpenSSH v9.5.P1</a>.</li>
<li>Comes with <a href="https://github.com/curl/curl/releases/tag/curl-8_4_0">cURL v8.4.0</a>.</li>
<li>Comes with <a href="https://github.com/openssl/openssl/releases/tag/openssl-3.1.4">OpenSSL v3.1.4</a>.</li>
<li>Comes with <a href="https://github.com/git-ecosystem/git-credential-manager/releases/tag/v2.4.1">Git Credential Manager v2.4.1</a>.</li>
<li>Comes with <a href="https://git.savannah.gnu.org/cgit/bash.git/commit/?id=2bb3cbefdb8fd019765b1a9cc42ecf37ff22fec6">Bash v5.2.21</a>.</li>
<li>Comes with <a href="https://github.com/mintty/mintty/releases/tag/3.7.0">MinTTY v3.7.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Symbolic links whose target is an absolute path <em>without</em> the drive prefix <a href="https://github.com/git-for-windows/git/issues/4586">accidentally had a drive prefix added when checked out</a>, rendering them "eternally modified". This bug <a href="https://github.com/git-for-windows/git/pull/4592">has been fixed</a>.</li>
<li>Git for Windows's installer <a href="https://github.com/git-for-windows/build-extra/pull/529">is no longer confused by global <code>GIT_*</code> environment variables</a>.</li>
<li>The installer <a href="https://github.com/git-for-windows/build-extra/pull/498">no longer claims that "fast-forward or merge" is the default <code>git pull</code> behavior</a>: The default behavior has changed in Git a while ago, to "fast-forward only".</li>
</ul>

</div><h2 id="v2.42.0(2)" nr="13" class="collapsible"> Changes in v2.42.0(2)<br /><small>since  v2.42.0 (August 21st 2023)</h2></small><div>

<p>As announced previously, Git for Windows will drop support for Windows 7 and for Windows 8 in one of the next versions, following <a href="https://www.msys2.org/docs/windows_support/">Cygwin's and MSYS2's lead</a> (Git for Windows relies on MSYS2 for components such as Bash and Perl).</p>

<p>Following the footsteps of the MSYS2 and Cygwin projects on which Git for Windows depends, the 32-bit variant of Git for Windows <a href="https://gitforwindows.org/32-bit.html">is being phased out</a>.</p>

<h3>Bug Fixes</h3>

<ul>
<li>Git for Windows v2.42.0's release notes claimed that it ships with Git LFS v3.4.0, <a href="https://github.com/git-for-windows/git/issues/4567">which is incorrect</a> and has been fixed in this release.</li>
<li>The installer option to enable support for Pseudo Consoles <a href="https://github.com/git-for-windows/git/issues/4571">has been handled incorrectly</a> since Git for Windows v2.41.0, which <a href="https://github.com/git-for-windows/build-extra/pull/522">has been fixed</a>.</li>
<li>Some Git commands (those producing paged output, for example) experienced a <a href="https://github.com/git-for-windows/git/issues/4459">significant slow-down</a> under certain circumstances, when running on a machine joined to a domain controller, which <a href="https://github.com/git-for-windows/MSYS2-packages/pull/124">has been fixed</a>.</li>
<li>As of Git for Windows v2.41.0, when installed into a location whose path contains non-ASCII characters, <a href="https://github.com/git-for-windows/git/issues/4573">it was no longer possible to fetch from/push to remote repositories via https://</a>, which <a href="https://github.com/git-for-windows/git/pull/4575">has been fixed</a>.</li>
</ul>

</div><h2 id="v2.42.0" nr="14" class="collapsible"> Changes in v2.42.0<br /><small>since  v2.41.0(3) (July 13th 2023)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.42.0/Documentation/RelNotes/2.42.0.txt">Git v2.42.0</a>.</li>
<li>Comes with <a href="https://curl.se/changes.html#8_2_1">cURL v8.2.1</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/3.4.0">Git LFS v3.4.0</a>.</li>
<li>Comes with <a href="https://github.com/openssl/openssl/releases/tag/openssl-3.1.2">OpenSSL v3.1.2</a>.</li>
<li>Comes with <a href="https://github.com/openssh/openssh-portable/releases/tag/V_9_4_P1">OpenSSH v9.4.P1</a>.</li>
<li>Comes with <a href="https://github.com/git-ecosystem/git-credential-manager/releases/tag/v2.3.2">Git Credential Manager v2.3.2</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>When <code>init.defaultBranch</code> is changed manually in the system config, subsequent Git for Windows upgrades <a href="https://github.com/git-for-windows/git/issues/4525">would overwrite that change</a>. This has been <a href="https://github.com/git-for-windows/build-extra/pull/515">fixed</a>.</li>
<li>When running on a remote APFS share, Git <a href="https://github.com/git-for-windows/git/issues/4482">would fail</a>, which <a href="https://github.com/git-for-windows/git/pull/4527">has been fixed</a>.</li>
</ul>

</div><h2 id="v2.41.0(3)" nr="15" class="collapsible"> Changes in v2.41.0(3)<br /><small>since  v2.41.0(2) (July 7th 2023)</h2></small><div>

<p>This release is a hot-fix release to incorporate a new Git Credential Manager version that addresses several issues present in the previous verison. There are no other changes.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git-ecosystem/git-credential-manager/releases/tag/v2.2.2">Git Credential Manager v2.2.2</a>.</li>
</ul>

</div><h2 id="v2.41.0(2)" nr="16" class="collapsible"> Changes in v2.41.0(2)<br /><small>since  v2.41.0 (June 1st 2023)</h2></small><div>

<p>As announced previously, Git for Windows will drop support for Windows 7 and for Windows 8 in one of the next versions, following <a href="https://www.msys2.org/docs/windows_support/">Cygwin's and MSYS2's lead</a> (Git for Windows relies on MSYS2 for components such as Bash and Perl).</p>

<p>Following the footsteps of the MSYS2 and Cygwin projects on which Git for Windows depends, the 32-bit variant of Git for Windows <a href="https://gitforwindows.org/32-bit.html">is being phased out</a>. As of Git for Windows v2.41.0, the 32-bit variant of the POSIX emulation layer (known as "MSYS2 runtime", powering Git Bash among other components shipped with Git for Windows) is in maintenance mode and will only see security bug fixes (if any). Users relying on 32-bit Git for Windows are highly encouraged to switch to the 64-bit version whenever possible.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/cygwin/cygwin/releases/tag/cygwin-3.4.7">MSYS2 runtime v3.4.7</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-3.1-notes.html">OpenSSL v3.1.1</a>, a major version upgrade (previously Git for Windows distributed OpenSSL v1.1.*).</li>
<li>To support interoperability with Windows Subsystem for Linux (WSL) better, it <a href="https://github.com/git-for-windows/git/pull/4438">is now possible to let Git set</a> e.g. the executable bits of files (this needs <code>core.WSLCompat</code> to be set, and <a href="https://devblogs.microsoft.com/commandline/chmod-chown-wsl-improvements/">the NTFS volume needs to be mounted in WSL using the appropriate options</a>).</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Portable Git: The Windows version is now parsed <a href="https://github.com/git-for-windows/build-extra/pull/506">more robustly</a> in the post-install script.</li>
<li>The labels of the File Explorer menu items installed by the Git for Windows installer <a href="https://github.com/git-for-windows/build-extra/pull/507">have been aligned</a> with what is customary ("Open Git Bash Here" instead of "Git Bash Here").</li>
</ul>

</div><h2 id="v2.41.0" nr="17" class="collapsible"> Changes in v2.41.0<br /><small>since  v2.40.1 (April 25th 2023)</h2></small><div>

<p>As announced previously, Git for Windows will drop support for Windows 7 and for Windows 8 in one of the next versions, following <a href="https://www.msys2.org/docs/windows_support/">Cygwin's and MSYS2's lead</a> (Git for Windows relies on MSYS2 for components such as Bash and Perl).</p>

<p>Following the footsteps of the MSYS2 and Cygwin projects on which Git for Windows depends, the 32-bit variant of Git for Windows <a href="https://gitforwindows.org/32-bit.html">is being phased out</a>. As of Git for Windows v2.41.0, the 32-bit variant of the POSIX emulation layer (known as "MSYS2 runtime", powering Git Bash among other components shipped with Git for Windows) is in maintenance mode and will only see security bug fixes (if any). Users relying on 32-bit Git for Windows are highly encouraged to switch to the 64-bit version whenever possible.</p>

<p>Please also note that the code-signing certificate used to sign Git for Windows' executables was renewed and may cause Smart Screen to show a warning until the certificate has gained a certain minimum reputation.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.41.0/Documentation/RelNotes/2.41.0.txt">Git v2.41.0</a>.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-9.3">OpenSSH v9.3p1</a></li>
<li>Comes with <a href="https://github.com/mintty/mintty/releases/tag/3.6.4">MinTTY v3.6.4</a>.</li>
<li>The Git for Windows installer now <a href="https://github.com/git-for-windows/build-extra/pull/491">also includes</a> the Git LFS documentation (i.e. <code>git help git-lfs</code> now works).</li>
<li>Comes with <a href="http://search.cpan.org/dist/perl-5.36.1/pod/perldelta.pod">Perl v5.36.1</a>.</li>
<li>Comes with <a href="https://dev.gnupg.org/source/gnupg/browse/STABLE-BRANCH-2-2/NEWS;gnupg-2.2.41?blame=off">GNU Privacy Guard v2.2.41</a>.</li>
<li>Comes with <a href="https://github.com/git-ecosystem/git-credential-manager/releases/tag/v2.1.2">Git Credential Manager v2.1.2</a>.</li>
<li>Comes with MSYS2 runtime (Git for Windows flavor) based on <a href="https://inbox.sourceware.org/cygwin-announce/20230214142733.1052688-1-corinna-cygwin@cygwin.com/">Cygwin 3.4.6</a>. (This does not extend to 32-bit Git for Windows, which <a href="https://github.com/git-for-windows/git/issues/4279">is stuck with v3.3.* of the MSYS2 runtime forever</a>.)</li>
<li>To help with Git for Windows' release mechanics, Git for Windows now ships <a href="https://github.com/git-for-windows/git/pull/4410">with two variants of <code>libcurl</code></a>.</li>
<li>Comes with <a href="https://curl.se/changes.html#8_1_2">cURL v8.1.2</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1u</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git GUI's <code>Repository&gt;Explore Working Copy</code> <a href="https://github.com/git-for-windows/git/issues/4356">was broken since v2.39.1</a>, which has been fixed.</li>
<li>The MSYS2 runtime was adjusted to <a href="https://github.com/git-for-windows/git/issues/4429">prepare for an upcoming Windows version</a>.</li>
</ul>

</div><h2 id="v2.40.1" nr="18" class="collapsible"> Changes in v2.40.1<br /><small>since  v2.40.0 (March 14th 2023)</h2></small><div>

<p>This is a security release, addressing <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-gq5x-v87v-8f7g">CVE-2023-29012</a>, <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-g4fv-xjqw-q7jm">CVE-2023-29011</a>, <a href="https://github.com/git/git/security/advisories/GHSA-v48j-4xgg-4844">CVE-2023-29007</a>, <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-9w66-8mq8-5vm8">CVE-2023-25815</a> and <a href="https://github.com/git/git/security/advisories/GHSA-2hvf-7c8p-28fx">CVE-2023-25652</a>.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.40.1/Documentation/RelNotes/2.40.1.txt">Git v2.40.1</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Addresses <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-gq5x-v87v-8f7g">CVE-2023-29012</a>, a vulnerability where starting Git CMD would execute <code>doskey.exe</code> in the current directory, if it exists.</li>
<li>Addresses <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-g4fv-xjqw-q7jm">CVE-2023-29011</a>, a vulnerability where the SOCKS5 proxy called <code>connect.exe</code> is susceptible to picking up an untrusted configuration on multi-user machines.</li>
<li>Addresses <a href="https://github.com/git/git/security/advisories/GHSA-v48j-4xgg-4844">CVE-2023-29007</a>, a vulnerability where <code>git submodule deinit</code> can inadvertently introduce malicious changes into the Git config file.</li>
<li>Addresses <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-9w66-8mq8-5vm8">CVE-2023-25815</a>, a vulnerability where Git can unexpectedly show crafted "localized" messages written by another user on a multi-user machine.</li>
<li>Addresses <a href="https://github.com/git/git/security/advisories/GHSA-2hvf-7c8p-28fx">CVE-2023-25652</a>, a vulnerability where <code>git apply --reject</code> could follow symbolic links to write files outside the worktree.</li>
</ul>

</div><h2 id="v2.40.0" nr="19" class="collapsible"> Changes in v2.40.0<br /><small>since  v2.39.2 (February 14th 2023)</h2></small><div>

<p>As announced previously, Git for Windows will drop support for Windows 7 and for Windows 8 in one of the next versions, following <a href="https://www.msys2.org/docs/windows_support/">Cygwin's and MSYS2's lead</a> (Git for Windows relies on MSYS2 for components such as Bash and Perl).</p>

<p>Also following the footsteps of the MSYS2 and Cygwin projects on which Git for Windows depends, the 32-bit variant of Git for Windows <a href="https://gitforwindows.org/32-bit.html">is nearing its end of support</a>.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.40.0/Documentation/RelNotes/2.40.0.txt">Git v2.40.0</a>.</li>
<li>In the olden Git days, there were "dashed" Git commands (e.g. <code>git-commit</code> instead of <code>git commit</code>). These haven't been supported for interactive use in a really, really long time. But they still worked in Git aliases and hooks ("scripts"). Since Git v1.5.4 (released on February 2nd, 2008), it was discouraged/deprecated to use dashed Git commands even in scripts. As of this version, Git for Windows <a href="https://github.com/git-for-windows/git/pull/4252">no longer supports these dashed commands</a>.</li>
<li>Comes with <a href="https://github.com/jonas/tig/releases/tag/tig-2.5.8">tig v2.5.8</a>.</li>
<li>Comes with <a href="https://tiswww.case.edu/php/chet/bash/NEWS">Bash v5.2 patchlevel 15</a>.</li>
<li>Comes with <a href="https://github.com/openssl/openssl/releases/tag/OpenSSL_1_1_1t">OpenSSL v1.1.1t</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnutls-help/2023-February/004816.html">GNU TLS v3.8.0</a>.</li>
<li>Comes with <a href="https://github.com/curl/curl/releases/tag/curl-7_88_1">cURL v7.88.1</a>.</li>
<li>Comes with <a href="https://github.com/Yubico/libfido2/releases/tag/1.13.0">libfido2 v1.13.0</a>.</li>
<li>Comes with <a href="https://github.com/GitCredentialManager/git-credential-manager/releases/tag/v2.0.935">Git Credential Manager v2.0.935</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Some commands mishandled absolute paths near the drive root (e.g. <a href="https://github.com/git-for-windows/git/issues/4200"><code>scalar unregister C:/foo</code></a>), which has been <a href="https://github.com/git-for-windows/git/pull/4253">fixed</a>.</li>
<li>When trying to call Cygwin (or for that matter, MSYS2) programs from Git Bash, users would frequently be greeted with <a href="https://github.com/git-for-windows/git/issues/4255">cryptic error messages about a "cygheap"</a> or even just an even more puzzling exit code 127. Many of these calls <a href="https://github.com/git-for-windows/msys2-runtime/pull/48">now</a> <a href="https://github.com/git-for-windows/msys2-runtime/pull/49">succeed</a>, allowing basic interactions. While it is still not possible for, say, Cygwin's <code>vim.exe</code> to interact with the Git Bash's terminal window, it <em>is</em> now possible for Cygwin's <code>zstd.exe</code> in conjuction with Git for Windows' <code>tar.exe</code> to handle <code>.tar.zst</code> archives. </li>
</ul>

</div><h2 id="v2.39.2" nr="20" class="collapsible"> Changes in v2.39.2<br /><small>since  v2.39.1 (January 17th 2023)</h2></small><div>

<p>This is a security release, addressing <a href="https://github.com/git/git/security/advisories/GHSA-gw92-x3fm-3g3q">CVE-2023-22490</a>, <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-p2x9-prp4-8gvq">CVE-2023-22743</a>, <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-wxwv-49qw-35pm">CVE-2023-23618</a> and <a href="https://github.com/git/git/security/advisories/GHSA-r87m-v37r-cwfh">CVE-2023-23946</a>.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.39.2/Documentation/RelNotes/2.39.2.txt">Git v2.39.2</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Addresses <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-p2x9-prp4-8gvq">CVE-2023-22743</a>, a vulnerability rated "high" making the Git for Windows' installer susceptible to DLL side-loading attacks.</li>
<li>Addresses <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-wxwv-49qw-35pm">CVE-2023-23618</a>, a vulnerability rated "high" where <code>gitk</code> would inadvertently execute programs placed in the worktree.</li>
<li>Addresses <a href="https://github.com/git/git/security/advisories/GHSA-gw92-x3fm-3g3q">CVE-2023-22490</a>, a moderate vulnerability allowing for data exfiltration in local clones.</li>
<li>Addresses <a href="https://github.com/git/git/security/advisories/GHSA-r87m-v37r-cwfh">CVE-2023-23946</a>, a moderate vulnerability that would allow crafted patches to trick <code>git apply</code> into writing into files outside the current directory.</li>
</ul>

</div><h2 id="v2.39.1" nr="21" class="collapsible"> Changes in v2.39.1<br /><small>since  v2.39.0(2) (December 21st 2022)</h2></small><div>

<p>This is a security release, addressing <a href="https://github.com/git/git/security/advisories/GHSA-475x-2q3q-hvwq">CVE-2022-41903</a>, <a href="https://github.com/git/git/security/advisories/GHSA-c738-c5qq-xg89">CVE-2022-23521</a> and <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-v4px-mx59-w99c">CVE-2022-41953</a>.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.39.1/Documentation/RelNotes/2.39.1.txt">Git v2.39.1</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Addresses <a href="https://github.com/git/git/security/advisories/GHSA-c738-c5qq-xg89">CVE-2022-23521</a>, a critical vulnerability in the <code>.gitattributes</code> parsing that potentially allows malicious code to be executed while cloning.</li>
<li>Addresses <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-v4px-mx59-w99c">CVE-2022-41953</a>, a vulnerability that makes Git GUI's <code>Clone</code> function susceptible to Remote Code Execution attacks.</li>
<li>Addresses <a href="https://github.com/git/git/security/advisories/GHSA-475x-2q3q-hvwq">CVE-2022-41903</a>, a vulnerability that may allow heap overflows and code to be executed inadvertently during a <code>git archive</code> invocation.</li>
<li>A <a href="https://github.com/git-for-windows/git/issues/4194">regression introduced in Git for Windows v2.39.0(2)</a> that prevented cloning from Bitbucket <a href="https://github.com/git-for-windows/MINGW-packages/pull/64">was fixed</a>.</li>
</ul>

</div><h2 id="v2.39.0(2)" nr="22" class="collapsible"> Changes in v2.39.0(2)<br /><small>since  v2.39.0 (December 12th 2022)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/PCRE2Project/pcre2/releases/tag/pcre2-10.42">PCRE2 v10.42</a>.</li>
<li>Comes with <a href="https://github.com/GitCredentialManager/git-credential-manager/releases/tag/v2.0.886">Git Credential Manager v2.0.886</a>.</li>
<li>Comes with <a href="https://github.com/mintty/mintty/releases/tag/3.6.3">MinTTY v3.6.3</a>.</li>
<li>Comes with <a href="https://github.com/curl/curl/releases/tag/curl-7_87_0">cURL v7.87.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The installer is expected to stop GPG agents automatically, but there was <a href="https://github.com/git-for-windows/git/issues/4172">a bug</a> that prevented that from working, which <a href="https://github.com/git-for-windows/build-extra/pull/453">has been fixed</a>.</li>
<li>A <a href="https://github.com/git-for-windows/git/issues/4171">regression</a> that caused <code>no_proxy</code> to be ignored was fixed by <a href="https://github.com/git-for-windows/git/issues/4191">upgrading libcurl</a>.</li>
<li>The Git Credential Manager version shipped with Git for Windows v2.39.0 <a href="https://github.com/git-for-windows/git/issues/4165">could not always find its UI helper</a> which was fixed by <a href="https://github.com/git-for-windows/git/issues/4166">upgrading to a fixed version</a>.</li>
<li>A bug in MinTTY caused it to throw a Critical Error when the printer spool service was not started, which was fixed by <a href="https://github.com/git-for-windows/git/issues/4182">upgrading MinTTY</a>.</li>
</ul>

</div><h2 id="v2.39.0" nr="23" class="collapsible"> Changes in v2.39.0<br /><small>since  v2.38.1 (October 18th 2022)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.39.0/Documentation/RelNotes/2.39.0.txt">Git v2.39.0</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1s</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_86_0">cURL v7.86.0</a>.</li>
<li>The Portable Git edition (which comes as a self-extracting 7-Zip archive) <a href="https://github.com/git-for-windows/build-extra/commit/0240a09014a4fcfd9f487e50d7a09464a2e428b8">now uses the latest 7-Zip version to self-extract</a>.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-9.1">OpenSSH v9.1p1</a>.</li>
<li>It <a href="https://github.com/git-for-windows/MSYS2-packages/commit/6823ee7b329b53f38747f64db8fb8d6de077a0e4">is now possible</a> to generate and use <a href="https://man.openbsd.org/ssh-keygen#FIDO_AUTHENTICATOR">SSH keys protected by security keys</a> (AKA FIDO devices) via Windows Hello, e.g. via <code>ssh-keygen.exe -t ecdsa-sk</code>.</li>
<li>Portable Git no longer configures <code>color.diff</code>, <code>color.status</code> and <code>color.branch</code> individually, but <a href="https://github.com/git-for-windows/build-extra/pull/442">configures <code>color.ui</code> instead</a>, which makes it easier to override the default.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnutls-help/2022-September/004765.html">GNU TLS v3.7.8</a>.</li>
<li>Comes with <a href="https://github.com/GitCredentialManager/git-credential-manager/releases/tag/v2.0.877">Git Credential Manager Core v2.0.877</a>.</li>
<li>Comes with <a href="https://github.com/mintty/mintty/releases/tag/3.6.2">MinTTY v3.6.2</a>.</li>
<li>Comes with <a href="https://tiswww.case.edu/php/chet/bash/NEWS">Bash v5.2 patchlevel 12</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v3.3.0">Git LFS v3.3.0</a>.</li>
<li>Comes with <a href="https://github.com/PCRE2Project/pcre2/blob/pcre2-10.41/ChangeLog">PCRE2 v10.41</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The Git executables (e.g. <code>git.exe</code> itself) used to have incomplete version information recorded in their resources, which <a href="https://github.com/git-for-windows/git/pull/4092">has been fixed</a>.</li>
<li>A <a href="https://github.com/git-for-windows/git/issues/4052">regression</a> introduced in Git for Windows v2.38.0 that prevented <code>git.exe</code> from running in Windows Nano Server containers <a href="https://github.com/git-for-windows/git/pull/4074">was fixed</a>.</li>
</ul>

</div><h2 id="v2.38.1" nr="24" class="collapsible"> Changes in v2.38.1<br /><small>since  v2.38.0 (October 3rd 2022)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.38.1/Documentation/RelNotes/2.38.1.txt">Git v2.38.1</a>.</li>
</ul>

</div><h2 id="v2.38.0" nr="25" class="collapsible"> Changes in v2.38.0<br /><small>since  v2.37.3 (August 30th 2022)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.38.0/Documentation/RelNotes/2.38.0.txt">Git v2.38.0</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_85_0">cURL v7.85.0</a>.</li>
<li>Comes with MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/pipermail/cygwin-announce/2022-September/010707.html">Cygwin 3.3.6</a>.</li>
<li>Comes with <a href="https://github.com/git-for-windows/busybox-w32/commit/985b51cf7">BusyBox v1.34.0.19688.985b51cf7</a>.</li>
<li>The <code>scalar</code> command is now included. <a href="https://github.com/microsoft/git/blob/vfs-2.37.3/contrib/scalar/docs/philosophy.md">Scalar</a> is a helper to automatically configure your (large) Git repositories to take advantage of the latest and greatest features. Note: If you work with repositories hosted on Azure Repos, use <a href="https://github.com/microsoft/git/releases/latest">Microsoft's fork of Git</a> for the best user experience.</li>
</ul>

</div><h2 id="v2.37.3" nr="26" class="collapsible"> Changes in v2.37.3<br /><small>since  v2.37.2(2) (August 11th 2022)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.37.3/Documentation/RelNotes/2.37.3.txt">Git v2.37.3</a>.</li>
<li>Comes with <a href="https://github.com/jonas/tig/releases/tag/tig-2.5.7">tig v2.5.7</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git for Windows <a href="https://github.com/git-for-windows/build-extra/pull/432">now correctly handles <code>.doc</code> files that are not Word Documents</a>.</li>
</ul>

</div><h2 id="v2.37.2(2)" nr="27" class="collapsible"> Changes in v2.37.2(2)<br /><small>since  v2.37.1 (July 12th 2022)</h2></small><div>

<h3>(Upcoming) breaking changes</h3>

<p>We updated the included Bash to version 5.1 (previously 4.4). Please check your shell scripts for potential compatibility issues.</p>

<p>Also, as previously announced, Git for Windows dropped support for Windows Vista.</p>

<p>Around the beginning of 2023, Git for Windows will drop support for Windows 7 and for Windows 8, following <a href="https://www.msys2.org/docs/windows_support/">Cygwin's and MSYS2's lead</a> (Git for Windows relies on MSYS2 for components such as Bash and Perl).</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.37.2/Documentation/RelNotes/2.37.2.txt">Git v2.37.2</a>.</li>
<li>Comes with <a href="https://github.com/jonas/tig/releases/tag/tig-2.5.6">tig v2.5.6</a>.</li>
<li>Comes with <a href="https://tiswww.case.edu/php/chet/bash/NEWS">Bash v5.1 patchlevel 016 </a>.</li>
<li>Comes with <a href="http://search.cpan.org/dist/perl-5.36.0/pod/perldelta.pod">Perl v5.36.0</a>.</li>
<li>Git's executables are <a href="https://github.com/git-for-windows/build-extra/pull/429">now</a> marked <a href="https://github.com/git-for-windows/git/pull/3942">Terminal Server-aware</a>, meaning: Git will be slightly faster when being run using Remote Desktop Services.</li>
<li><code>git svn</code> is now based on <a href="https://svn.apache.org/repos/asf/subversion/tags/1.14.2/CHANGES">subversion v1.14.2</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnutls-help/2022-July/004746.html">GNU TLS v3.7.7</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git for Windows <a href="https://github.com/git-for-windows/build-extra/pull/430">now ships without the <code>zmore</code> and <code>bzmore</code> utilities</a> (which were broken and included only inadvertently).</li>
<li>A <a href="https://github.com/git-for-windows/git/issues/3945">regression in the <code>vimdiff</code> mode of <code>git mergetool</code></a> has been <a href="https://github.com/git-for-windows/git/pull/3960">fixed</a>.</li>
<li>With certain network drives, <a href="https://github.com/git-for-windows/git/issues/3727">it was reported</a> that some attributes associated with caching confused Git for Windows. This <a href="https://github.com/git-for-windows/git/pull/3753">was fixed</a>.</li>
</ul>

</div><h2 id="v2.37.1" nr="28" class="collapsible"> Changes in v2.37.1<br /><small>since  v2.37.0 (June 27th 2022)</h2></small><div>

<p>This release addresses <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-gjrj-fxvp-hjj2">CVE-2022-31012</a> and <a href="https://github.com/git/git/security/advisories/GHSA-j342-m5hw-rr3v">CVE-2022-29187</a>.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.37.1/Documentation/RelNotes/2.37.1.txt">Git v2.37.1</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1q</a>.</li>
<li>Comes with <a href="https://github.com/GitCredentialManager/git-credential-manager/releases/tag/v2.0.785">Git Credential Manager Core v2.0.785</a>.</li>
<li>Comes with <a href="https://github.com/jonas/tig/releases/tag/tig-2.5.5">tig v2.5.5</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Pasting large amounts of text in Git for Windows' Bash when running inside Windows Terminal <a href="https://github.com/git-for-windows/git/issues/3936">often resulted in garbled text</a>, which has been fixed.</li>
<li>The Perl module <a href="https://metacpan.org/source/ATOOMIC/Clone-0.45/Changes">perl-Clone</a> which linked to a non-existing DLL was rebuilt to fix the issue.</li>
<li>The Git for Windows installer can no longer be tricked into running an untrusted <code>git.exe</code> in elevated mode (<a href="https://github.com/git-for-windows/git/security/advisories/GHSA-gjrj-fxvp-hjj2">CVE-2022-31012</a>).</li>
<li>When running Git in a world-writable directory owned by the current user (think <code>C:\Windows\Temp</code>, when running under the <code>SYSTEM</code> account), the checks for dubious ownership of the <code>.git</code> directory now detect this situation properly (<a href="https://github.com/git/git/security/advisories/GHSA-j342-m5hw-rr3v">CVE-2022-29187</a>).</li>
</ul>

</div><h2 id="v2.37.0" nr="29" class="collapsible"> Changes in v2.37.0<br /><small>since  v2.36.1 (May 9th 2022)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.37.0/Documentation/RelNotes/2.37.0.txt">Git v2.37.0</a>.</li>
<li>Many anti-malware products seem to have problems with our MSYS2 runtime, leading to problems running e.g. <code>git subtree</code>. We <a href="https://github.com/git-for-windows/msys2-runtime/pull/37">added a workaround</a> that hopefully helps in most of these scenarios.</li>
<li>Comes with MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/pipermail/cygwin-announce/2022-May/010565.html">Cygwin 3.3.5</a>.</li>
<li>Comes with <a href="https://raw.githubusercontent.com/PCRE2Project/pcre2/pcre2-10.40/ChangeLog">PCRE2 v10.40</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v3.2.0">Git LFS v3.2.0</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnutls-help/2022-May/004744.html">GNU TLS v3.7.6</a>.</li>
<li>SSH's CBC ciphers, which were re-enabled in 2017 to better support Azure Repos <a href="https://github.com/git-for-windows/build-extra/pull/421">have again been disabled by default</a> because Azure Repos does not require them any longer.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1p</a>.</li>
<li>Comes with <a href="https://github.com/GitCredentialManager/git-credential-manager/releases/tag/v2.0.779">Git Credential Manager Core v2.0.779</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_84_0">cURL v7.84.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The Git for Windows-only <code>--show-ignored-directory</code> option of <code>git status</code>, which was deprecated a long time ago, <a href="https://github.com/git-for-windows/git/pull/2067">was finally removed</a>.</li>
<li>A crash when running Git for Windows in Wine <a href="https://github.com/git-for-windows/git/pull/3875">was fixed</a>.</li>
<li>A bug in the interaction between FSCache and parallel checkout <a href="https://github.com/git-for-windows/git/pull/3909">was fixed</a>.</li>
<li>Cloning to network shares failed on some network file systems, which was <a href="https://github.com/git-for-windows/git/pull/3646">fixed</a>.</li>
<li>When Git indicates an unsafe directory due to the file system (e.g. FAT32) being unable to record ownership, Git <a href="https://github.com/git-for-windows/git/pull/3887">now gives better hints</a>.</li>
</ul>

</div><h2 id="v2.36.1" nr="30" class="collapsible"> Changes in v2.36.1<br /><small>since  v2.36.0 (April 20th 2022)</h2></small><div>

<h3>Upcoming breaking changes</h3>

<p>We plan to update the included bash to version 5.1 (currently 4.4) soon after Git for Windows 2.36.0 is released. Please check your shell scripts for potential compatibility issues.</p>

<p>Git for Windows will also stop supporting Windows Vista soon after Git for Windows 2.36.0 is released. Around the beginning of 2023, Git for Windows will drop support for Windows 7 and for Windows 8, following <a href="https://www.msys2.org/docs/windows_support/">Cygwin's and MSYS2's lead</a> (Git for Windows relies on MSYS2 for components such as Bash and Perl).</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.36.1/Documentation/RelNotes/2.36.1.txt">Git v2.36.1</a>.</li>
<li>On newer Windows versions, Git <a href="https://github.com/git-for-windows/git/pull/3751">now assumes a Win32 Console with full color capabilities</a>. This helps e.g. when NeoVIM is configured as Git's editor.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-9.0">OpenSSH v9.0p1</a>.</li>
<li>When <code>git clean</code> fails due to long paths, <a href="https://github.com/git-for-windows/git/pull/3817">Git now advises the user to set <code>core.longPaths</code></a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_83_0">cURL v7.83.0</a>.</li>
<li>Git Credential Manager's binaries <a href="https://github.com/git-for-windows/build-extra/pull/406">are no longer installed in the same location as core Git's own dashed programs</a>. This separates more clearly the core Git executables from the Git executables provided by third-parties.</li>
<li>Comes with <a href="https://github.com/GitCredentialManager/git-credential-manager/releases/tag/v2.0.696">Git Credential Manager Core v2.0.696</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1o</a>.</li>
<li>Comes with <a href="https://github.com/git-for-windows/msys2-runtime/commit/d72d5e8aeb7df99c55bdc438fb71fdeffd2bd1e5">patch level 4</a> of the MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/pipermail/cygwin-announce/2022-January/010438.html">Cygwin 3.3.4</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>A regression introduced in Git for Windows v2.36.0 where GPG in 32-bit versions simply would not work <a href="https://github.com/git-for-windows/MSYS2-packages/commit/002b641e4409ce76709419e835e1fb2a6de14e7c">was fixed</a>.</li>
<li>The <code>proxy-lookup</code> helper <a href="https://github.com/git-for-windows/git/issues/3818">only reported the first letter of the proxy</a>, which was fixed.</li>
<li>The installer <a href="https://github.com/git-for-windows/build-extra/pull/329">now verifies that .NET Framework 4.7.2 is available</a> before offering Git Credential Manager (GCM) as an option (because it is required for GCM to work).</li>
<li>A bug introduced into v2.36.0 where <a href="https://github.com/git-for-windows/git/issues/3825">shell scripts failed to run on some network shares with the error "Too many levels of symbolic links"</a> was fixed.</li>
</ul>

</div><h2 id="v2.36.0" nr="31" class="collapsible"> Changes in v2.36.0<br /><small>since  v2.35.3 (April 15th 2022)</h2></small><div>

<p>This version includes Git LFS v3.1.4, addressing <a href="https://github.com/git-lfs/git-lfs/security/advisories/GHSA-6rw3-3whw-jvjj">CVE-2022-24826</a> (if you use Git LFS with <a href="https://github.com/git-for-windows/git/wiki/MinGit">MinGit</a>, you will want to upgrade).</p>

<h3>Upcoming breaking changes</h3>

<p>We plan to update the included bash to version 5.1 (currently 4.4) soon after Git for Windows 2.36.0 is released. Please check your shell scripts for potential compatibility issues.</p>

<p>Git for Windows will also stop supporting Windows Vista soon after Git for Windows 2.36.0 is released. Around the beginning of 2023, Git for Windows will drop support for Windows 7 and for Windows 8, following <a href="https://www.msys2.org/docs/windows_support/">Cygwin's and MSYS2's lead</a> (Git for Windows relies on MSYS2 for components such as Bash and Perl).</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.36.0/Documentation/RelNotes/2.36.0.txt">Git v2.36.0</a>.</li>
<li>Comes with MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/pipermail/cygwin-announce/2022-January/010438.html">Cygwin 3.3.4</a>.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-8.9">OpenSSH v8.9p1</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_82_0">cURL v7.82.0</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1n</a>.</li>
<li>Comes with <a href="https://github.com/GitCredentialManager/git-credential-manager/releases/tag/v2.0.696">Git Credential Manager Core v2.0.696</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnutls-help/2022-March/004738.html">GNU TLS v3.7.4</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v3.1.4">Git LFS v3.1.4</a>.</li>
</ul>

</div><h2 id="v2.35.3" nr="32" class="collapsible"> Changes in v2.35.3<br /><small>since  v2.35.2 (April 12th 2022)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.35.3/Documentation/RelNotes/2.35.3.txt">Git v2.35.3</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The advice indicating how to use the <code>%(prefix)</code> with a network share path <a href="https://github.com/git-for-windows/git/pull/3790">was updated</a> to use the appropriate number of slashes.</li>
<li><a href="https://github.com/git-for-windows/git/pull/3791">Various fixes</a> for usage of the <code>safe.directory</code> and <code>%(prefix)</code> when using Windows Subsystem for Linux (WSL).</li>
</ul>

</div><h2 id="v2.35.2" nr="33" class="collapsible"> Changes in v2.35.2<br /><small>since  v2.35.1(2) (February 1st 2022)</h2></small><div>

<p>This version addresses <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-vw2c-22j4-2fh2">CVE-2022-24765</a> and <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-gf48-x3vr-j5c3">CVE-2022-24767</a>.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.35.2/Documentation/RelNotes/2.35.2.txt">Git v2.35.2</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The uninstaller was hardened to <a href="https://github.com/git-for-windows/git/security/advisories/GHSA-gf48-x3vr-j5c3">avoid a vulnerability when running under the SYSTEM account</a>, addressing CVE-2022-24767.</li>
</ul>

</div><h2 id="v2.35.1(2)" nr="34" class="collapsible"> Changes in v2.35.1(2)<br /><small>since  v2.35.1 (January 29th 2022)</h2></small><div>

<h3>Bug Fixes</h3>

<ul>
<li>A <a href="https://github.com/git-for-windows/git/issues/3674">bug</a> in FSCache that triggered by a patch that made it into Git for Windows v2.35.0 <a href="https://github.com/git-for-windows/git/pull/3678">was fixed</a>.</li>
</ul>

</div><h2 id="v2.35.1" nr="35" class="collapsible"> Changes in v2.35.1<br /><small>since  v2.35.0 (January 24th 2022)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.35.1/Documentation/RelNotes/2.35.1.txt">Git v2.35.1</a>.</li>
</ul>

</div><h2 id="v2.35.0" nr="36" class="collapsible"> Changes in v2.35.0<br /><small>since  v2.34.1 (November 25th 2021)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.35.0/Documentation/RelNotes/2.35.0.txt">Git v2.35.0</a>.</li>
<li>Comes with a version of the MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/pipermail/cygwin-announce/2021-December/010338.html">Cygwin 3.3.3</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1m</a>.</li>
<li>Comes with <a href="https://github.com/GitCredentialManager/git-credential-manager/releases/tag/v2.0.632">Git Credential Manager Core v2.0.632.34631</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_81_0">cURL v7.81.0</a>.</li>
<li>Comes with <a href="https://github.com/jonas/tig/releases/tag/tig-2.5.5">tig v2.5.5</a>.</li>
<li>Comes with <a href="https://github.com/git-for-windows/msys2-runtime/commit/b600e8ead500aef55e23810c2e630d9be46f3a4c">patch level 4</a> of the MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/pipermail/cygwin-announce/2021-December/010338.html">Cygwin 3.3.3</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>A <a href="https://github.com/git-for-windows/git/issues/3624">bug</a> which caused crashes when running <code>git log</code> with custom date formats in 32-bit builds was fixed.</li>
</ul>

</div><h2 id="v2.34.1" nr="37" class="collapsible"> Changes in v2.34.1<br /><small>since  v2.34.0 (November 15th 2021)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.34.1/Documentation/RelNotes/2.34.1.txt">Git v2.34.1</a>.</li>
<li>Comes with <a href="https://github.com/microsoft/git-credential-manager-core/releases/tag/v2.0.605">Git Credential Manager Core v2.0.605.12951</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_80_0">cURL v7.80.0</a>.</li>
</ul>

</div><h2 id="v2.34.0" nr="38" class="collapsible"> Changes in v2.34.0<br /><small>since  v2.33.1 (October 13th 2021)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.34.0/Documentation/RelNotes/2.34.0.txt">Git v2.34.0</a>.</li>
<li>Config settings referring to paths relative to where Git is installed <a href="https://github.com/git-for-windows/git/pull/3472">now have to be marked via <code>%(prefix)/</code> instead of the now-deprecated leading slash</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v3.0.2">Git LFS v3.0.2</a>.</li>
<li>Contains <a href="https://github.com/git-for-windows/git/pull/3492">new, experimental support for <code>core.fsyncObjectFiles=batch</code></a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Configuring a system-wide VS Code as Git's editor <a href="https://github.com/git-for-windows/git/issues/3471">was broken</a>, which has been fixed.</li>
<li>It is <a href="https://github.com/git-for-windows/git/pull/3487">now possible</a> to clone files larger than 4GB as long as they are transferred via <a href="https://git-lfs.github.io/">Git LFS</a>.</li>
<li>Git now works around <a href="https://github.com/microsoft/terminal/issues/9359">an issue with <code>vi</code> and incorrect line breaks in the Windows Terminal</a>.</li>
</ul>

</div><h2 id="v2.33.1" nr="39" class="collapsible"> Changes in v2.33.1<br /><small>since  v2.33.0(2) (August 24th 2021)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.33.1/Documentation/RelNotes/2.33.1.txt">Git v2.33.1</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1l</a>.</li>
<li>The included <code>git svn</code> now uses <a href="https://svn.apache.org/repos/asf/subversion/tags/1.14.1/CHANGES">subversion v1.14.1</a> internally.</li>
<li><a href="https://github.com/microsoft/Git-Credential-Manager-for-Windows">Git Credential Manager for Windows</a> (which was superseded by <a href="https://aka.ms/gcmcore">Git Credential Manager Core</a>, and was deprecated for a long time now, and no longer succeeds to authenticate with GitHub) is <a href="https://github.com/git-for-windows/build-extra/pull/377">no longer included in Git for Windows</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_79_1">cURL v7.79.1</a>.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-8.8">OpenSSH v8.8p1</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v3.0.1">Git LFS v3.0.1</a>.</li>
<li>The built-in filesystem watcher ("FSMonitor") <a href="https://github.com/git-for-windows/git/pull/3447">has been updated to the latest version</a>.</li>
<li>Comes with <a href="https://github.com/microsoft/git-credential-manager-core/releases/tag/v2.0.567">Git Credential Manager Core v2.0.567.18224</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Wordpad <a href="https://github.com/git-for-windows/build-extra/pull/378">can be configured as Git's preferred editor</a> again.</li>
<li>A bug where Git's garbage collection during a <code>git pull</code> failed to delete obsolete files <a href="https://github.com/git-for-windows/git/pull/3415">was fixed</a>.</li>
<li>The <code>git svn</code> command, <a href="https://github.com/git-for-windows/git/issues/3392">which was broken in Git for Windows v2.33.0(2)</a>, has been fixed.</li>
<li>The password prompt when cloning via SSH <a href="https://github.com/git-for-windows/build-extra/pull/381">works again</a>.</li>
<li>The MSYS2 runtime <a href="https://github.com/git-for-windows/msys2-runtime/pull/33">no longer complains about FAST_CWD on Windows/ARM64</a>.</li>
<li>When VS Code is configured as editor, <a href="https://github.com/git-for-windows/git/issues/3452">it no longer needs the window to be closed, just the tab</a>.</li>
<li>The 32-bit versions of Git for Windows included outdated versions of <code>ca-certificates</code> and <code>less</code>, <a href="https://github.com/git-for-windows/MSYS2-packages/pull/49">which has been rectified</a>.</li>
</ul>

</div><h2 id="v2.33.0(2)" nr="40" class="collapsible"> Changes in v2.33.0(2)<br /><small>since  v2.33.0 (August 17th 2021)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_78_0">cURL v7.78.0</a>.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-8.7">OpenSSH v8.7p1</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>A <a href="https://github.com/git-for-windows/git/issues/3368">bug</a> affecting older Windows versions that caused the installer to show the error message "Could not call proc" <a href="https://github.com/git-for-windows/build-extra/pull/374">was fixed</a>.</li>
</ul>

</div><h2 id="v2.33.0" nr="41" class="collapsible"> Changes in v2.33.0<br /><small>since  v2.32.0(2) (July 6th 2021)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.33.0/Documentation/RelNotes/2.33.0.txt">Git v2.33.0</a>.</li>
<li>Comes with <a href="http://search.cpan.org/dist/perl-5.34.0/pod/perldelta.pod">Perl v5.34.0</a> (and some updated Perl modules).</li>
<li>It is <a href="https://github.com/git-for-windows/build-extra/pull/367">now possible</a> to ask Git for Windows to use an SSH found on the <code>PATH</code> instead of its bundled OpenSSH executable.</li>
<li>Comes with <a href="https://github.com/microsoft/git-credential-manager-core/releases/tag/v2.0.498">Git Credential Manager Core v2.0.498.54650</a>.</li>
<li>The experimental FSMonitor patches were replaced with <a href="https://github.com/git-for-windows/git/pull/3350">a newer version</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnupg-announce/2021q3/000461.html">GNU Privacy Guard v2.2.29</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The installer no longer <a href="https://github.com/git-for-windows/git/issues/3312">shows an error dialog</a> when upgrading while the Windows Terminal Profile option is checked.</li>
<li>Interaction with <a href="https://gerrit.googlesource.com/git-repo/">the <code>git repo</code> tool</a> was <a href="https://github.com/git-for-windows/git/pull/3328">improved</a>.</li>
<li>The version of GNU Privacy Guard (GPG) bundled in Git for Windows <a href="https://github.com/git-for-windows/git/issues/2888">did not work in 64-bit setups</a>, which <a href="https://github.com/git-for-windows/MSYS2-packages/pull/46">was fixed</a>.</li>
</ul>

</div><h2 id="v2.32.0(2)" nr="42" class="collapsible"> Changes in v2.32.0(2)<br /><small>since  v2.32.0 (June 7th 2021)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>The Windows Terminal profile is now identified <a href="https://github.com/git-for-windows/build-extra/pull/356">by a GUID</a>, for more robust customization.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnupg-announce/2021q2/000460.html">GNU Privacy Guard v2.2.28</a>.</li>
<li>Comes with <a href="https://github.com/microsoft/git-credential-manager-core/releases/tag/v2.0.475">Git Credential Manager Core v2.0.475.64295</a>.</li>
<li>Access to remote HTTPS repositories that requires client certificates <a href="https://github.com/git-for-windows/git/issues/3292">can be enabled</a>. This is now necessary because <a href="https://github.com/curl/curl/commit/54e747501626b81149b1b44949119d365db82004">cURL no longer sends client certificates by default</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The built-in file system watcher could hang in some scenarios. <a href="https://github.com/git-for-windows/git/pull/3263">This was fixed</a>.</li>
<li>Remote HTTPS repositories <a href="https://github.com/git-for-windows/git/issues/3266">could not be accessed from within portable Git installed into a network share</a>. This <a href="https://github.com/git-for-windows/MINGW-packages/pull/51">has been fixed</a>.</li>
<li>When scrolling in the pager (e.g. in the output of <code>git log</code>), <a href="https://github.com/git-for-windows/git/issues/3235">lines were duplicated by mistake</a>. This was fixed.</li>
<li>The <code>git subtree</code> command was <a href="https://github.com/git-for-windows/git/issues/3260">completely broken in the previous release</a>, and was fixed.</li>
<li>A bug was fixed where remote operations <a href="https://github.com/git-for-windows/git/issues/3268">appeared to hang</a> (but were waiting for user feedback on a hidden Console).</li>
<li>A bug was fixed where the experimental built-in file system watcher had <a href="https://github.com/git-for-windows/git/issues/3262">a problem with worktrees whose paths had non-ASCII characters</a>.</li>
</ul>

</div><h2 id="v2.32.0" nr="43" class="collapsible"> Changes in v2.32.0<br /><small>since  v2.31.1 (March 27th 2021)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.32.0/Documentation/RelNotes/2.32.0.txt">Git v2.32.0</a>.</li>
<li>The installer now offers to install <a href="https://github.com/git-for-windows/build-extra/pull/339">a Windows Terminal profile</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_77_0">cURL v7.77.0</a>.</li>
<li>Comes with <a href="https://pcre.org/news.txt">PCRE2 v10.37</a>.</li>
<li>The experimental, built-in <a href="https://github.com/git-for-windows/git/discussions/3251">file system monitor</a> is now <a href="https://github.com/git-for-windows/build-extra/pull/351">featured as an experimental option in the installer</a>.</li>
<li>Comes with <a href="https://github.com/microsoft/git-credential-manager-core/releases/tag/v2.0.474">Git Credential Manager Core v2.0.474.41365</a>.</li>
<li>Sublime Text 4 <a href="https://github.com/git-for-windows/build-extra/pull/355">now gets detected by the installer</a>.</li>
<li>Comes with <a href="https://github.com/jonas/tig/releases/tag/tig-2.5.4">tig v2.5.4</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>When testing a custom editor in the installer, <a href="https://github.com/git-for-windows/git/issues/3155">we now spawn it in non-elevated mode</a>, fixing e.g. Atom when an instance is already running.</li>
<li>The meta credential-helper used by the Portable Git edition of Git for Windows <a href="https://github.com/git-for-windows/git/issues/3196">sometimes crashed</a>, which has been fixed.</li>
<li>The auto-updater <a href="https://github.com/git-for-windows/build-extra/pull/347">no longer suggests to downgrade from -rc0 versions</a>.</li>
</ul>

</div><h2 id="v2.31.1" nr="44" class="collapsible"> Changes in v2.31.1<br /><small>since  v2.31.0 (March 15th 2021)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.31.1/Documentation/RelNotes/2.31.1.txt">Git v2.31.1</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnupg-announce/2021q1/000452.html">GNU Privacy Guard v2.2.27</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1k</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.13.3">Git LFS v2.13.3</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>It <a href="https://github.com/git-for-windows/git/issues/2675">is now possible</a> to execute the Windows Store version of <code>python3.exe</code> from Git Bash.</li>
</ul>

</div><h2 id="v2.31.0" nr="45" class="collapsible"> Changes in v2.31.0<br /><small>since  v2.30.2 (March 9th 2021)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.31.0/Documentation/RelNotes/2.31.0.txt">Git v2.31.0</a>.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-8.5">OpenSSH v8.5p1</a>.</li>
<li>Comes with <a href="https://github.com/jonas/tig/releases/tag/tig-2.5.3">tig v2.5.3</a>.</li>
<li>Git for Windows now ships with <a href="https://github.com/git-for-windows/git/pull/3082">an experimental built-in file-system monitor</a>, without the need to install Watchman and setting <code>core.fsmonitor</code>. It can be turned on by setting both <code>feature.manyFiles=true</code> <em>and</em> <code>feature.experimental=true</code> (or directly, via <code>core.useBuiltinFSMonitor=true</code>).</li>
<li>Comes with <a href="https://github.com/microsoft/git-credential-manager-core/releases/tag/v2.0.394-beta">Git Credential Manager Core v2.0.394.50751</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnutls-help/2021-March/004698.html">GNU TLS v3.7.1</a>.</li>
</ul>

</div><h2 id="v2.30.2" nr="46" class="collapsible"> Changes in v2.30.2<br /><small>since  v2.30.1 (February 9th 2021)</h2></small><div>

<p>This version addresses CVE-2021-21300 (a bug that allows code injection during a clone from an untrusted source).</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.30.2/Documentation/RelNotes/2.30.2.txt">Git v2.30.2</a>.</li>
<li>Comes with <a href="https://pcre.org/news.txt">PCRE2 v10.36</a>.</li>
<li>Comes with <a href="https://github.com/jonas/tig/releases/tag/tig-2.5.2">tig v2.5.2</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1j</a>.</li>
</ul>

</div><h2 id="v2.30.1" nr="47" class="collapsible"> Changes in v2.30.1<br /><small>since  v2.30.0(2) (January 14th 2021)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.30.1/Documentation/RelNotes/2.30.1.txt">Git v2.30.1</a>.</li>
<li>Comes with <a href="http://search.cpan.org/dist/perl-5.32.1/pod/perldelta.pod">Perl v5.32.1</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_75_0">cURL v7.75.0</a>.</li>
</ul>

</div><h2 id="v2.30.0(2)" nr="48" class="collapsible"> Changes in v2.30.0(2)<br /><small>since  v2.30.0 (December 28th 2020)</h2></small><div>

<p>This version includes <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.13.2">Git LFS v2.13.2</a>, addressing CVE-2021-21237.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/microsoft/git-credential-manager-core/releases/tag/v2.0.318-beta">Git Credential Manager Core v2.0.318.44100</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.13.2">Git LFS v2.13.2</a>.</li>
</ul>

</div><h2 id="v2.30.0" nr="49" class="collapsible"> Changes in v2.30.0<br /><small>since  v2.29.2(3) (December 8th 2020)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.30.0/Documentation/RelNotes/2.30.0.txt">Git v2.30.0</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1i</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_74_0">cURL v7.74.0</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.13.1">Git LFS v2.13.1</a>.</li>
<li>Notepad and Wordpad are <a href="https://github.com/git-for-windows/build-extra/pull/304">now supported</a> as editors without manual configuration.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The auto-updater <a href="https://github.com/git-for-windows/build-extra/pull/318">now shows the progress while installing</a>.</li>
<li>The credential-helper selector (which is the default credential helper in the Portable version of Git for Windows) <a href="https://github.com/git-for-windows/build-extra/pull/319">now handles paths with spaces correctly</a>.</li>
</ul>

</div><h2 id="v2.29.2(3)" nr="50" class="collapsible"> Changes in v2.29.2(3)<br /><small>since  v2.29.2(2) (November 4th 2020)</h2></small><div>

<p>This version updates Git Credential Manager Core to address <a href="https://github.com/microsoft/Git-Credential-Manager-Core/security/advisories/GHSA-2gq7-ww4j-3m76">CVE-2020-26233</a>.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnupg-announce/2020q4/000450.html">GNU Privacy Guard v2.2.25</a>.</li>
<li>Comes with <a href="https://github.com/microsoft/git-credential-manager-core/releases/tag/v2.0.289-beta">Git Credential Manager Core v2.0.289.48418</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Beyond Compare 4 <a href="https://github.com/git-for-windows/git/issues/2893">can be configured as difftool <code>bc4</code> again</a>.</li>
</ul>

</div><h2 id="v2.29.2(2)" nr="51" class="collapsible"> Changes in v2.29.2(2)<br /><small>since  v2.29.2 (October 30th 2020)</h2></small><div>

<p>This version includes a new Git LFS version to fix <a href="https://github.com/git-lfs/git-lfs/security/advisories/GHSA-4g4p-42wc-9f3m">CVE-2020-27955</a>.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/microsoft/git-credential-manager-core/releases/tag/v2.0.280-beta">Git Credential Manager Core v2.0.280.19487</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.12.1">Git LFS v2.12.1</a>.</li>
</ul>

</div><h2 id="v2.29.2" nr="52" class="collapsible"> Changes in v2.29.2<br /><small>since  v2.29.1 (October 23rd 2020)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.29.2/Documentation/RelNotes/2.29.2.txt">Git v2.29.2</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The recent regression where OpenSSH's <code>copy-ssh-id</code> <a href="https://github.com/git-for-windows/git/issues/2873">failed to work correctly</a>, was <a href="https://github.com/git-for-windows/MSYS2-packages/pull/40">fixed</a>.</li>
<li>A <a href="https://github.com/git-for-windows/git/issues/2874">regression preventing <code>/usr/bin/update-ca-trust</code> from working</a> was fixed.</li>
</ul>

</div><h2 id="v2.29.1" nr="53" class="collapsible"> Changes in v2.29.1<br /><small>since  v2.29.0 (October 19th 2020)</h2></small><div>

<p>Important note: v2.29.0 and v2.29.1 upgrade existing users of <a href="https://github.com/microsoft/Git-Credential-Manager-for-Windows/">Git Credential Manager for Windows</a> (which was just deprecated) to <a href="https://github.com/microsoft/Git-Credential-Manager-Core">Git Credential Manager Core</a> ("GCM Core", which is the designated successor of the former). This is necessary because <a href="https://github.blog/changelog/2019-08-08-password-based-http-basic-authentication-deprecation-and-removal/">GitHub deprecated password-based authentication</a> and intends to remove support for it soon, and GCM Core is prepared for this change.</p>

<p>Also, as of v2.29.0, the option to override the branch name used by <code>git init</code> for the initial branch is <a href="https://github.com/git-for-windows/build-extra/pull/307">featured prominently</a> in the installer.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.29.1/Documentation/RelNotes/2.29.1.txt">Git v2.29.1</a>.</li>
<li>The MSYS2 runtime <a href="https://github.com/msys2/msys2-runtime/pull/16">now optionally supports creating Cygwin-style symbolic links</a> (via setting the environment variable <code>MSYS=winsymlinks:sysfile</code>).</li>
</ul>

</div><h2 id="v2.29.0" nr="54" class="collapsible"> Changes in v2.29.0<br /><small>since  v2.28.0 (July 28th 2020)</h2></small><div>

<p>This version upgrades existing users of <a href="https://github.com/microsoft/Git-Credential-Manager-for-Windows/">Git Credential Manager for Windows</a> (which was just deprecated) to <a href="https://github.com/microsoft/Git-Credential-Manager-Core">Git Credential Manager Core</a> ("GCM Core", which is the designated successor of the former). This is necessary because <a href="https://github.blog/changelog/2019-08-08-password-based-http-basic-authentication-deprecation-and-removal/">GitHub deprecated password-based authentication</a> and intends to remove support for it soon, and GCM Core is prepared for this change.</p>

<p>Also, the option to override the branch name used by <code>git init</code> for the initial branch is now <a href="https://github.com/git-for-windows/build-extra/pull/307">featured prominently</a> in the installer.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.29.0/Documentation/RelNotes/2.29.0.txt">Git v2.29.0</a>.</li>
<li>Comes with MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/pipermail/cygwin-announce/2020-August/009678.html">Cygwin 3.1.7</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.12.0">Git LFS v2.12.0</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnupg-announce/2020q3/000448.html">GNU Privacy Guard v2.2.23</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1h</a>.</li>
<li>Comes with <a href="https://github.com/PJK/libcbor/releases/tag/0.8.0">libcbor v0.8.0</a>.</li>
<li>Comes with <a href="https://github.com/Yubico/libfido2/releases/tag/1.5.0">libfido2 v1.5.0</a>.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-8.4">OpenSSH v8.4p1</a>.</li>
<li>Comes with <a href="https://github.com/microsoft/git-credential-manager-core/releases/tag/v2.0.252-beta">Git Credential Manager Core v2.0.252.766</a>.</li>
<li>Existing Git Credential Manager for Windows users are now <a href="https://github.com/git-for-windows/build-extra/pull/305">automatically upgraded</a> to <a href="https://github.com/microsoft/git-credential-manager-core/">Git Credential Manager Core</a>.</li>
<li>Git for Windows' installer learned to <a href="https://github.com/git-for-windows/build-extra/pull/307">let users override the default branch used by <code>git init</code></a>.</li>
<li><a href="https://github.com/git-for-windows/build-extra/pull/309">The installer size was reduced</a> by dropping a couple unneeded <code>.dll</code> files.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_73_0">cURL v7.73.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The credential helper selector (used as default credential helper in the Portable Git) <a href="https://github.com/git-for-windows/git/issues/2776">now persists the users choice correctly again</a>.</li>
<li>The full command-lines of MSYS2 processes (such as <code>cp.exe</code>) spawned from Git's Bash <a href="https://github.com/git-for-windows/git/issues/2756">can now be seen in <code>sysmon</code>, <code>wmic</code> etc</a> by default.</li>
<li>A <a href="https://github.com/git-for-windows/git/issues/2738">bug</a> preventing Unicode characters from being used in the window title of Git Bash was fixed.</li>
<li>OpenSSH was patched to no longer <a href="https://github.com/git-for-windows/git/issues/2743">warn about an "invalid format"</a> when private and public keys are stored separately.</li>
<li>Non-ASCII output of paged Git commands <a href="https://github.com/git-for-windows/git/pull/2834">is now rendered correctly in Windows Terminal</a>.</li>
<li>It is <a href="https://github.com/git-for-windows/build-extra/pull/303">now possible</a> to use <code>wordpad.exe</code> as Git's editor of choice.</li>
<li>When using Git via the "Run As..." function, <a href="https://github.com/git-for-windows/git/pull/2725">it now uses the correct home directory</a>.</li>
<li>The Git Bash prompt <a href="https://github.com/git-for-windows/git/pull/2800">now works even after calling <code>set -u</code></a>.</li>
<li>Git for Windows <a href="https://github.com/git-for-windows/build-extra/pull/312">can now be installed</a> even with stale <code>AutoRun</code> registry entries (e.g. left-overs from a Miniconda installation).</li>
</ul>

</div><h2 id="v2.28.0" nr="55" class="collapsible"> Changes in v2.28.0<br /><small>since  v2.27.0 (June 1st 2020)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.28.0/Documentation/RelNotes/2.28.0.txt">Git v2.28.0</a>.</li>
<li>Comes with <a href="https://svn.apache.org/repos/asf/subversion/tags/1.14.0/CHANGES">subversion v1.14.0</a>.</li>
<li><a href="https://github.com/git-for-windows/build-extra/pull/294">Comes with the designated successor</a> of Git Credential Manager for Windows (GCM for Windows), <a href="https://github.com/microsoft/git-credential-manager-core">the cross-platform Git Credential Manager Core</a>. For now, this is opt-in, with the idea of eventually retiring GCM for Windows.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_71_1">cURL v7.71.1</a>.</li>
<li>Comes with <a href="http://search.cpan.org/dist/perl-5.32.0/pod/perldelta.pod">Perl v5.32.0</a>.</li>
<li>Comes with MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/pipermail/cygwin-announce/2020-July/009605.html">Cygwin 3.1.6</a> (including the improvements of <a href="https://cygwin.com/pipermail/cygwin-announce/2020-June/009561.html">Cygwin 3.1.5</a>).</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnupg-announce/2020q3/000446.html">GNU Privacy Guard v2.2.21</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>A typo <a href="https://github.com/git-for-windows/build-extra/pull/291">was fixed</a> in the installer.</li>
<li>The new <code>git pull</code> behavior option <a href="https://github.com/git-for-windows/build-extra/pull/292">now records the <code>fast-forward</code> choice correctly</a>.</li>
<li>In v2.27.0, <a href="https://github.com/git-for-windows/git/issues/2649"><code>git svn</code> was broken completely</a>, which has been fixed.</li>
<li>Some Git operations <a href="https://github.com/git-for-windows/git/issues/2653">could end up with bogus modified symbolic links</a> (where <code>git status</code> would report changes but <code>git diff</code> would not), which is now fixed.</li>
<li>When reinstalling (or upgrading) Git for Windows, <a href="https://github.com/git-for-windows/build-extra/pull/295">the "Pseudo Console Support" choice is now remembered correctly</a>.</li>
<li>Under certain circumstances, the Git Bash window (MinTTY) <a href="https://github.com/git-for-windows/git/issues/2687">would crash frequently</a>, which has been addressed.</li>
<li>When pseudo console support is enabled, <a href="https://github.com/git-for-windows/git/issues/2689">the VIM editor sometimes had troubles accepting certain keystrokes</a>, which was fixed.</li>
<li>Due to a bug, it was not possible to disable Pseudo Console support by reinstalling with the checkbox turned off, <a href="https://github.com/git-for-windows/build-extra/pull/299">which has been fixed</a>.</li>
<li>A bug with enabled Pseudo Console support, where <code>git add -i</code> <a href="https://github.com/git-for-windows/git/issues/2729">would not quit the file selection mode upon an empty input</a>, has been fixed.</li>
<li>The cleanup mode called "scissors" in <code>git commit</code> <a href="https://github.com/git-for-windows/git/pull/2714">now handles CR/LF line endings correctly</a>.</li>
<li>When cloning into an existing directory, under certain circumstances, the <code>core.worktree</code> option was set unnecessarily. <a href="https://github.com/git-for-windows/git/pull/2731">This has been fixed</a>.</li>
</ul>

</div><h2 id="v2.27.0" nr="56" class="collapsible"> Changes in v2.27.0<br /><small>since  v2.26.2 (April 20th 2020)</h2></small><div>

<p>Due to <a href="https://github.com/git-for-windows/git/pull/2637">a bug when handling symbolic links that was fixed in this version</a>, <code>git status</code> will show symbolic links as modified even as <code>git diff</code> won't report any changes. The quickest work-around is to call <code>git add -u</code> which lets Git realize that nothing changed, actually.</p>

<p>This release comes with a Git Bash that optionally uses <a href="https://devblogs.microsoft.com/commandline/windows-command-line-introducing-the-windows-pseudo-console-conpty/">Windows-native pseudo consoles</a>. Meaning: finally, Git Bash can accommodate console programs like <code>node.exe</code>, Python or PHP, without using the <code>winpty</code> helper (see <a href="#known-issues"><em>Known Issues</em> above</a>). Note that this is still a very new feature and is therefore known to have some corner-case bugs.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.27.0/Documentation/RelNotes/2.27.0.txt">Git v2.27.0</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1g</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_70_0">cURL v7.70.0</a>.</li>
<li>Comes with <a href="https://svn.apache.org/repos/asf/subversion/tags/1.13.0/CHANGES">subversion v1.13.0</a>.</li>
<li>Comes with MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/ml/cygwin-announce/2020-02/msg00006.html">Cygwin 3.1.4</a>.</li>
<li>The release notes <a href="https://github.com/git-for-windows/build-extra/pull/281">have been made a bit more readable and are now linked from the Start Menu group</a>.</li>
<li>The Frequently Asked Questions (FAQ) <a href="https://github.com/git-for-windows/build-extra/pull/283">are now linked in a Start Menu item</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.11.0">Git LFS v2.11.0</a>.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-8.3">OpenSSH v8.3p1</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Some Perl packages (e.g. <code>Net::SSLeay</code>) that <a href="https://github.com/git-for-windows/git/issues/2598">had been broken recently</a> have been fixed.</li>
<li>Git for Windows and WSL Git <a href="https://github.com/git-for-windows/git/pull/2637">now have the same idea of symbolic links' length</a>, i.e. <code>git status</code> will no longer mark them as modified in Git for Windows after checking them out in WSL.</li>
</ul>

</div><h2 id="v2.26.2" nr="57" class="collapsible"> Changes in v2.26.2<br /><small>since  v2.26.1 (April 9th 2020)</h2></small><div>

<p>Yet another security fix release: With a crafted URL that contains a newline or empty host, or lacks a scheme, the credential helper machinery can be fooled into providing credential information that is not appropriate for the protocol in use and host being contacted (CVE-2020-11008).</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.26.2/Documentation/RelNotes/2.26.2.txt">Git v2.26.2</a>.</li>
<li>Comes with <a href="https://github.com/jonas/tig/releases/tag/tig-2.5.1">tig v2.5.1</a>.</li>
<li>Worktree updates (e.g. <code>git checkout</code>, <code>git reset --hard</code>) <a href="https://github.com/git-for-windows/git/pull/2589">got a performance boost in sparse checkouts</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>A recent regression in <code>gitk</code> that prevented it from running in bare repositories <a href="https://github.com/git-for-windows/git/pull/2549">has been fixed</a>.</li>
</ul>

</div><h2 id="v2.26.1" nr="58" class="collapsible"> Changes in v2.26.1<br /><small>since  v2.26.0 (March 23rd 2020)</h2></small><div>

<p>This includes a fix for CVE-2020-5260.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.26.1/Documentation/RelNotes/2.26.1.txt">Git v2.26.1</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1f</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git <a href="https://github.com/git-for-windows/git/pull/2574">now accepts more date formats</a> such as <code>%g</code> and <code>%V</code>.</li>
</ul>

</div><h2 id="v2.26.0" nr="59" class="collapsible"> Changes in v2.26.0<br /><small>since  v2.25.1 (February 19th 2020)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.26.0/Documentation/RelNotes/2.26.0.txt">Git v2.26.0</a>.</li>
<li>Git for Windows' OpenSSH <a href="https://github.com/git-for-windows/git/issues/2525">now can use USB security tokens</a> (e.g. Yubikeys).</li>
<li>The native Windows HTTPS backend (Secure Channel) <a href="https://github.com/git-for-windows/git/pull/2535">has learned to work gracefully with Fiddler and corporate proxies</a>.</li>
<li>Git for Windows' release notes <a href="https://github.com/git-for-windows/build-extra/commit/3b89da01f46dc03417329c3702fc233622313397">have been made a bit easier to read/navigate</a>.</li>
<li>The Free/Libre <a href="https://vscodium.com/">VSCodium</a> version of <a href="https://code.visualstudio.com">Visual Studio Code</a> is now <a href="https://github.com/git-for-windows/build-extra/pull/278">also detected</a> as an option for the default Git editor.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_69_1">cURL v7.69.1</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1e</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnupg-announce/2020q1/000444.html">GNU Privacy Guard v2.2.20</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git for Windows <a href="https://github.com/git-for-windows/git/pull/2533">can now clone into directories the current user can write to, even if they lack permission to even read the parent directory</a>.</li>
<li>When asking for a password via Git GUI, <a href="https://github.com/git-for-windows/git/issues/2215">non-ASCII characters are now handled correctly</a>.</li>
<li><code>git update-git-for-windows -y</code> <a href="https://github.com/git-for-windows/build-extra/pull/279">now is fully automatable</a>.</li>
</ul>

</div><h2 id="v2.25.1" nr="60" class="collapsible"> Changes in v2.25.1<br /><small>since  v2.25.0 (January 13th 2020)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.25.1/Documentation/RelNotes/2.25.1.txt">Git v2.25.1</a>.</li>
<li>The Portable version of Git for Windows <a href="https://github.com/git-for-windows/git/issues/2467">now defaults to turning on the FSCache</a> just like the installer does.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.10.0">Git LFS v2.10.0</a>.</li>
<li>Portable Git <a href="https://github.com/git-for-windows/git/issues/2493">can now be run from a RAM disk</a>, too.</li>
<li>The deprecation of <code>Git CMD</code> <a href="https://github.com/git-for-windows/build-extra/pull/275">has been reverted</a>: the security issue (<code>git show</code> would execute a <code>git</code> executable or script in the current directory instead of the intended <code>git.exe</code>) was fixed already in v2.20.0.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-8.2">OpenSSH v8.2p1</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Some corner-case bugs in the built-in <code>git add -i</code> <a href="https://github.com/git-for-windows/git/issues/2466">were fixed</a>.</li>
<li>The file name <code>COM0</code> <a href="https://github.com/git-for-windows/git/issues/2470">is no longer mistaken for a reserved file name</a>.</li>
<li>The <code>curl.exe</code> included in Git for Windows <a href="https://github.com/git-for-windows/git/issues/2491">can access SFTP/SSH hosts again</a>.</li>
</ul>

</div><h2 id="v2.25.0" nr="61" class="collapsible"> Changes in v2.25.0<br /><small>since  v2.24.1(2) (December 10th 2019)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.25.0/Documentation/RelNotes/2.25.0.txt">Git v2.25.0</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnupg-announce/2019q4/000443.html">GNU Privacy Guard v2.2.19</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.9.2">Git LFS v2.9.2</a>.</li>
<li>When upgrading Git for Windows, by default the installer <a href="https://github.com/git-for-windows/build-extra/pull/270">now only shows pages with previously-unseen options</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_68_0">cURL v7.68.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The startup file for GNU nano, which had been included with DOS line endings (and therefore upset <code>nano</code>) <a href="https://github.com/git-for-windows/git/issues/2429">is now included with Unix line endings again</a>.</li>
<li>Git for Windows now <a href="https://github.com/git-for-windows/git/pull/2440">fails as expected</a> when trying to check out files with illegal characters in their file names.</li>
<li>Git <a href="https://github.com/git-for-windows/git/pull/2449">now works properly</a> when inside a symlinked work tree.</li>
<li>Repositories with old commits containing backslashes in file names <a href="https://github.com/git-for-windows/git/pull/2437">can now be fetched/cloned again</a> (but Git will still refuse to check out files with backslashes in their file names).</li>
<li>Git GUI <a href="https://github.com/git-for-windows/git/pull/2452">can now deal with uninitialized submodules</a> (this was a Windows-specific bug).</li>
<li>It is <a href="https://github.com/git-for-windows/git/issues/2435">again possible</a> to clone repositories where <em>some</em> past revision contained file names containing backslashes (Git will of course still refuse to check out such revisions).</li>
</ul>

</div><h2 id="v2.24.1(2)" nr="62" class="collapsible"> Changes in v2.24.1(2)<br /><small>since  v2.24.0(2) (November 6th 2019)</h2></small><div>

<p>This is a security bug release that fixes CVE-2019-1348, CVE-2019-1349, CVE-2019-1350, CVE-2019-1351, CVE-2019-1352, CVE-2019-1353, CVE-2019-1354, CVE-2019-1387, and CVE-2019-19604.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.24.1/Documentation/RelNotes/2.24.1.txt">Git v2.24.1</a>.</li>
<li>Comes with <a href="https://github.com/jonas/tig/releases/tag/tig-2.5.0">tig v2.5.0</a>.</li>
<li>Comes with <a href="https://github.com/git-for-windows/msys2-runtime/commit/1bfdf956dae03d59bfe44b1e5882403ab803a67b">patch level 4</a> of the MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/ml/cygwin-announce/2019-04/msg00030.html">Cygwin 3.0.7</a>.</li>
<li>The command-line options of <code>git-bash.exe</code> <a href="https://github.com/git-for-windows/MINGW-packages/pull/36">are now documented</a> (call <code>git help git-bash</code>).</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.9.1">Git LFS v2.9.1</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_67_0">cURL v7.67.0</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnupg-announce/2019q4/000442.html">GNU Privacy Guard v2.2.18</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>MinGit <a href="https://github.com/git-for-windows/build-extra/pull/267">no longer overrides an installed Git for Windows' system gitconfig</a>.</li>
<li>The "Check daily for updates" feature <a href="https://github.com/git-for-windows/build-extra/pull/268">uses the Action Center again</a>.</li>
<li>When associating <code>.sh</code> files with Git Bash to allow running them by double-clicking them in the Windows Explorer, shell scripts with non-ASCII characters in their file name <a href="https://github.com/git-for-windows/git/issues/2189">are now supported</a>.</li>
</ul>

</div><h2 id="v2.24.0(2)" nr="63" class="collapsible"> Changes in v2.24.0(2)<br /><small>since  v2.24.0 (November 4th 2019)</h2></small><div>

<h3>Bug Fixes</h3>

<ul>
<li>Using <code>http.extraHeader</code> <a href="https://github.com/gitgitgadget/git/pull/453">no longer results in spurious crashes</a>.</li>
<li>The <code>/proc/{stdin,stdout,stderr}</code> pseudo-symlinks <a href="https://github.com/git-for-windows/build-extra/pull/265">are now installed properly even with non-US locales</a>.</li>
<li>A bug <a href="https://github.com/git-for-windows/git/pull/2391">was fixed</a> that prevented <code>gitk</code> from refreshing after new changes were committed.</li>
<li>A bug in cURL v7.67.0 that caused <code>SSL_read: No error</code> with some servers <a href="https://github.com/git-for-windows/MINGW-packages/commit/7b39ea818c014bafcd7c75f6aefd614fef756164">was fixed</a>.</li>
</ul>

</div><h2 id="v2.24.0" nr="64" class="collapsible"> Changes in v2.24.0<br /><small>since  v2.23.0 (August 17th 2019)</h2></small><div>

<p>Note! As a consequence of making <code>git config --system</code> work as expected, the location of the system config is now <code>C:\Program Files\Git\etc\gitconfig</code> (no longer split between <code>C:\Program Files\Git\mingw64\etc\gitconfig</code> and <code>C:\ProgramData\Git\config</code>), and likewise the location of the system gitattributes is now <code>C:\Program Files\Git\etc\gitattributes</code> (no longer <code>C:\Program Files\Git\mingw64\etc\gitattributes</code>). Any manual modifications to <code>C:\ProgramData\Git\config</code> need to be ported manually.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.24.0/Documentation/RelNotes/2.24.0.txt">Git v2.24.0</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_66_0">cURL v7.66.0</a>.</li>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/1.20.0">Git Credential Manager v1.20.0</a>.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-8.1">OpenSSH v8.1p1</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1d</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.9.0">Git LFS v2.9.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The shell construct <code>&lt;(&lt;command&gt;)</code>, which was broken in v2.23.0 (<code>/dev/fd/&lt;n&gt;: no such file or directory</code>), <a href="https://github.com/git-for-windows/build-extra/pull/255">was fixed</a>.</li>
<li>The default config <a href="https://github.com/git-for-windows/build-extra/pull/256">no longer skips <code>git-lfs</code> downloads</a>.</li>
<li>Starting with cURL v7.66.0, <a href="https://github.com/curl/curl/commit/f9c7ba9096ec29db2536481d8e9ebe314e007f0c"><code>$HOME/.netrc</code> can be used</a> instead of <code>$HOME/_netrc</code> (but it will still fall back to looking for the latter).</li>
<li>The installer's "ProductVersion" <a href="https://github.com/git-for-windows/build-extra/pull/257">is now consistent with older Git for Windows versions'</a>.</li>
<li><a href="https://github.com/git-for-windows/git/pull/2358">Makes <code>git config --system</code> work like you think it should</a>.</li>
<li>The (still experimental) built-in <code>git add -p</code> <a href="https://github.com/git-for-windows/git/pull/2368">no longer gets confused about incomplete lines</a> (i.e. a file's l last line that does not end in a Line Feed).</li>
<li>A buffer overrun in the code to determine which files need to be marked as hidden <a href="https://github.com/git-for-windows/git/pull/2371">was plugged</a>.</li>
<li>The support for <code>sendpack.sideband</code> that was removed by mistake <a href="https://github.com/git-for-windows/git/pull/2375">was re-introduced</a>, to support <code>git push</code> via the <code>git://</code> protocol again.</li>
<li><code>git stash</code> <a href="https://github.com/git-for-windows/git/pull/2378">no longer records skip-worktree files as deleted</a> after resolving merge conflicts in them.</li>
<li>The Git for Windows installer <a href="https://github.com/git-for-windows/build-extra/pull/264">no longer complains about a downgrade</a> when upgrading from an <code>-rc</code> version, i.e. from a pre-release leading up to the next major version.</li>
</ul>

</div><h2 id="v2.23.0" nr="65" class="collapsible"> Changes in v2.23.0<br /><small>since  v2.22.0 (June 8th 2019)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.23.0/Documentation/RelNotes/2.23.0.txt">Git v2.23.0</a>.</li>
<li>Comes with <a href="https://github.com/git-for-windows/msys2-runtime/commit/e0e7936faa74acea8cde0f89f464402515d1caad">patch level 3</a> of the MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/ml/cygwin-announce/2019-04/msg00030.html">Cygwin 3.0.7</a>.</li>
<li>Comes with <a href="https://pcre.org/changelog.txt">PCRE2 v10.33</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnupg-announce/2019q3/000439.html">GNU Privacy Guard v2.2.17</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_65_3">cURL v7.65.3</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.8.0">Git LFS v2.8.0</a>.</li>
<li>When configuring Git for Windows to use <code>plink</code>, <a href="https://github.com/git-for-windows/build-extra/pull/251">there is now a checkbox specifically for TortoisePlink</a>.</li>
<li>The FSCache feature <a href="https://github.com/git-for-windows/git/pull/2224">is now used with <code>git checkout</code> and <code>git reset</code> in sparse checkouts</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git for Windows' MSYS2 runtime was <a href="https://github.com/git-for-windows/msys2-runtime/commit/c10b4185a35f494a2ff4ad2f5828540d93d56bec">patched</a> to fix a bug where setting the environment variable <code>SHELL</code> to an empty string in a shell script would not only fail to pass that setting to non-MSYS2 processes (such as <code>git.exe</code>) but also completely skip all environment variables that sort after said variable.</li>
<li><code>git clean -dfx</code> <a href="https://github.com/git-for-windows/git/pull/2268">no longer follows NTFS junction points (also known as mount points)</a>.</li>
<li>A <a href="https://github.com/git-for-windows/git/pull/2253">workaround</a> now allows cloning to certain network drives (e.g. Isilon).</li>
<li>Fixed <a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-1211">CVE-2019-1211</a> in MinGit/Portable Git by being more careful about validating the Windows-wide config.</li>
</ul>

</div><h2 id="v2.22.0" nr="66" class="collapsible"> Changes in v2.22.0<br /><small>since  v2.21.0 (February 26th 2019)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.22.0/Documentation/RelNotes/2.22.0.txt">Git v2.22.0</a>.</li>
<li>The <code>awk</code> included in Git for Windows <a href="https://github.com/git-for-windows/build-extra/pull/232">now includes extensions</a> such as <code>inplace</code>.</li>
<li>The file/product version stored in the installer's <code>.exe</code> file <a href="https://github.com/git-for-windows/build-extra/pull/235">now matches the version of the included <code>git.exe</code> file's</a>.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-8.0">OpenSSH v8.0p1</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.7.2">Git LFS v2.7.2</a>.</li>
<li>Comes with MSYS2 runtime (Git for Windows flavor) based on Cygwin v3.x (see release notes for Cygwin <a href="https://cygwin.com/ml/cygwin-announce/2019-02/msg00010.html">3.0.0</a>, <a href="https://cygwin.com/ml/cygwin-announce/2019-02/msg00014.html">3.0.1</a>, <a href="https://cygwin.com/ml/cygwin-announce/2019-03/msg00002.html">3.0.2</a>, <a href="https://cygwin.com/ml/cygwin-announce/2019-03/msg00008.html">3.0.3</a>, <a href="https://cygwin.com/ml/cygwin-announce/2019-03/msg00016.html">3.0.4</a>, <a href="https://cygwin.com/ml/cygwin-announce/2019-03/msg00051.html">3.0.5</a>, <a href="https://cygwin.com/ml/cygwin-announce/2019-04/msg00012.html">3.0.6</a>, and <a href="https://cygwin.com/ml/cygwin-announce/2019-04/msg00030.html">3.0.7</a>).</li>
<li>There are now <a href="https://github.com/git-for-windows/git/pull/2150">experimental built-in versions of <code>git add -i</code> and <code>git add -p</code></a>, i.e. those modes are now a lot faster (in particular at startup). You can opt into using them on the last installer page.</li>
<li>PortableGit <a href="https://github.com/git-for-windows/git/issues/2116">now comes with a meta credential helper</a>, i.e. a GUI that lets the user choose <em>which</em> of the available credential helpers to use. This should help to avoid storing credentials on other people's machines when running portable Git from a thumb drive.</li>
<li>Comes with <a href="http://git.savannah.gnu.org/cgit/gawk.git/plain/NEWS?h=gawk-5.0.0">gawk v5.0.0</a>.</li>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/1.19.0">Git Credential Manager v1.19.0</a>.</li>
<li>Comes with <a href="https://github.com/petervanderdoes/gitflow-avh/releases/tag/1.12.3">git-flow v1.12.3</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1c</a>.</li>
<li>Comes with <a href="https://lists.gnupg.org/pipermail/gnupg-announce/2019q2/000438.html">GNU Privacy Guard v2.2.16</a>, specifically <a href="https://github.com/git-for-windows/MSYS2-packages/pull/33">patched to handle Windows paths</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_65_1">cURL v7.65.1</a>.</li>
<li>Comes with <a href="http://h5l.org/releases.html">Heimdal v7.5.0</a>.
-packages/pull/33).</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git for Windows' updater <a href="https://github.com/git-for-windows/build-extra/pull/234">is now accessible</a>, i.e. it can be read by a screen reader.</li>
<li><code>git update-git-for-windows</code> (i.e. the auto updater of Git for Windows) now <a href="https://github.com/git-for-windows/build-extra/pull/239">reports correctly when it failed to access the GitHub API</a>.</li>
<li>Git for Windows' updater <a href="https://github.com/git-for-windows/build-extra/pull/242">no longer runs into GitHub API rate limits</a> (this used to be quite common in enterprise scenarios, where many users would share one IP as far as GitHub is concerned).</li>
<li>gitk <a href="https://github.com/git-for-windows/git/pull/2170">no longer fails with "filename too long"</a> when there are 1,000+ branches/tags.</li>
<li>A bug which on occasion caused lengthy rebase runs to crash without error message <a href="https://github.com/git-for-windows/git/pull/2182">was fixed</a>.</li>
<li>Two workarounds from the Git for Windows 1.x era (concerning reading credentials via GUI and fetching via <code>git://</code>) <a href="https://github.com/git-for-windows/git/pull/2178">were considered obsolete</a>.</li>
<li><code>git difftool --no-index</code> <a href="https://github.com/git-for-windows/git/pull/2175">can now be run outside of Git worktrees</a>.</li>
<li><code>git rebase -i</code> used to get confused when an <code>exec</code> command created new commits and then appended <code>pick</code> lines for them. This <a href="https://github.com/git-for-windows/git/pull/2121">has been fixed</a>.</li>
<li>During a run of <code>git rebase --rebase-merges</code>, the output of <code>git status</code> <a href="https://github.com/git-for-windows/git/pull/2185">now shows <code>label</code> lines correctly</a>, i.e. with the labels' names instead of the commit hash they point to.</li>
<li>We <a href="https://github.com/git-for-windows/git/pull/2198">now avoid problems updating the commit graph</a> when <code>gc.writeCommitGraph=true</code>.</li>
</ul>

</div><h2 id="v2.21.0" nr="67" class="collapsible"> Changes in v2.21.0<br /><small>since  v2.20.1 (December 15th 2018)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.21.0/Documentation/RelNotes/2.21.0.txt">Git v2.21.0</a>.</li>
<li>The custom editor setting in the installer <a href="https://github.com/git-for-windows/build-extra/pull/221">has been improved substantially</a>.</li>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/1.18.4.0">Git Credential Manager v1.18.4.0</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_64_0">cURL v7.64.0</a>.</li>
<li>Comes with <a href="https://github.com/petervanderdoes/gitflow-avh/releases/tag/1.12.0">git-flow v1.12.0</a>.</li>
<li><code>git archive</code> <a href="https://github.com/git-for-windows/git/pull/2077">no longer requires <code>gzip</code> to generate <code>.tgz</code> archives</a> (this means in particular that it works in MinGit).</li>
<li>System-wide Sublime Text installations <a href="https://github.com/git-for-windows/build-extra/commit/396b283cc6231589b0b034d4ca4b241b25163e9a">are now detected</a> and offered on the editor wizard page.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.7.1">Git LFS v2.7.1</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The <code>Git CMD</code> deprecation <a href="https://github.com/git-for-windows/build-extra/pull/222">was further clarified</a> to mention that the <em>Start Menu item</em> is deprecated, not using Git from CMD.</li>
<li>Certain drivers/anti-malware caused <code>git.exe</code> to hang, which <a href="https://github.com/git-for-windows/MINGW-packages/pull/32">has been fixed</a>.</li>
<li><code>git stash</code> <a href="https://github.com/git-for-windows/git/issues/2006">now works</a> after staging files with <code>git add -N</code>.</li>
<li>A problem with <code>difftool</code> and more than a handful modified files <a href="https://github.com/git-for-windows/git/pull/2026">has been fixed</a>.</li>
<li>The regression where <code>git-cmd &lt;command&gt;</code> would not execute the command <a href="https://github.com/git-for-windows/git/issues/2039">was fixed</a>.</li>
<li>Portable Git <a href="https://github.com/git-for-windows/git/issues/2036">can be launched via network paths again</a>.</li>
<li>FSCache works again <a href="https://github.com/git-for-windows/git/issues/2022">on network drives</a>, in particular <a href="https://github.com/git-for-windows/git/issues/1989">when Windows 8.1 or older</a> are involved.</li>
<li>Partially hidden text in the <code>Path</code> options page in the installer <a href="https://github.com/git-for-windows/git/issues/2049">is no longer hidden</a>.</li>
<li>Fixes <a href="https://github.com/git-for-windows/git/issues/1993">an obscure <code>git svn</code> hang</a>.</li>
<li>The installer <a href="https://github.com/git-for-windows/git/issues/2011">now configures editors so that the built-in rebase can use them</a>.</li>
</ul>

</div><h2 id="v2.20.1" nr="68" class="collapsible"> Changes in v2.20.1<br /><small>since  v2.20.0 (December 10th 2018)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.20.1/Documentation/RelNotes/2.20.1.txt">Git v2.20.1</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_63_0">cURL v7.63.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li><a href="https://github.com/git-for-windows/git/pull/1983">Fixes</a> a speed regression in the built-in rebase.</li>
</ul>

</div><h2 id="v2.20.0" nr="69" class="collapsible"> Changes in v2.20.0<br /><small>since  v2.19.2 (November 21st 2018)</h2></small><div>

<p>Please note that Git for Windows v2.19.2 was offered as a full release only for about a week, and then demoted to "pre-release" status, as it had two rather big regressions: 32-bit Git Bash crashed, and git:// was broken.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.20.0/Documentation/RelNotes/2.20.0.txt">Git v2.20.0</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.1.1-notes.html">OpenSSL v1.1.1a</a>. The OpenSSH, cURL and Heimdal packages were rebuilt to make use of OpenSSL v1.1.1a.</li>
<li>The FSCache feature <a href="https://github.com/git-for-windows/git/pull/1937">was further optimized in particular for very large repositories</a>.</li>
<li>To appease certain anti-malware, MinTTY was recompiled with a patch to avoid <a href="https://github.com/git-for-windows/MSYS2-packages/commit/63f68558c9c6a6c7765c18dacbbcac328748eb30">GCC trampolines</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.6.1">Git LFS v2.6.1</a>.</li>
<li>Comes with <a href="https://tiswww.case.edu/php/chet/bash/NEWS">Bash v4.4 patchlevel 023 </a>.</li>
<li>Commands to interact with CVS repositories were considered obsolete <a href="https://github.com/git-for-windows/build-extra/commit/59b521a3b">and have been removed</a>.</li>
<li>The desired HTTP version (HTTP/2 or HTTP/1.1) <a href="https://github.com/git-for-windows/git/pull/1968">can now be configured via the <code>http.version</code> setting</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git CMD <a href="https://github.com/git-for-windows/git/issues/1945">no longer picks up <code>git.exe</code> from the current directory (if any)</a>.</li>
<li>Git Bash <a href="https://github.com/git-for-windows/MINGW-packages/commit/deb0395d031401ffe55024fb066267e2ea8d032b">works again in 32-bit Git for Windows</a>.</li>
<li>Git can now <a href="https://github.com/git-for-windows/git/issues/1949">access <code>git://</code> remotes again</a>.</li>
<li>The confusing descriptions of the PATH options in the installer <a href="https://github.com/git-for-windows/build-extra/pull/216">were clarified</a>.</li>
<li>A bug in the <code>notepad</code> support in conjunction with line wrapping <a href="https://github.com/git-for-windows/build-extra/pull/218">was fixed</a>.</li>
<li>Comes two backported fixes to <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/issues/812">allow NTLM/Kerberos authentication to fall back to HTTP/1.1</a>.</li>
<li>It is <a href="https://github.com/git-for-windows/git/issues/1650">now possible to call <code>cmd\git.exe</code> via a symbolic link</a>.</li>
</ul>

</div><h2 id="v2.19.2" nr="70" class="collapsible"> Changes in v2.19.2<br /><small>since  v2.19.1 (Oct 5th 2018)</h2></small><div>

<ul>
<li>The <em>Git CMD</em> start menu shortcut is deprecated and will be dropped in future version. Note that the deprecation only affects the shortcut; <code>git-cmd.exe</code> will continue to be distributed and installed.</li>
</ul>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.19.2/Documentation/RelNotes/2.19.2.txt">Git v2.19.2</a>.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-7.9">OpenSSH v7.9p1</a>.</li>
<li>The description of the editor option to choose Vim <a href="https://github.com/git-for-windows/build-extra/pull/207">has been clarified</a> to state that this <em>unsets</em> <code>core.editor</code>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_62_0">cURL v7.62.0</a>.</li>
<li>The type of symlinks to create (directory or file) <a href="https://github.com/git-for-windows/git/pull/1897">can now be specified via the <code>.gitattributes</code></a>.</li>
<li>The FSCache feature <a href="https://github.com/git-for-windows/git/pull/1908">now uses a faster method to enumerate files</a>, making e.g. <code>git status</code> faster in large repositories.</li>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/1.18.3">Git Credential Manager v1.18.3</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.6.0">Git LFS v2.6.0</a>.</li>
<li>Comes with MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/ml/cygwin-announce/2018-11/msg00007.html">Cygwin 2.11.2</a>.</li>
<li>The FSCache feature <a href="https://github.com/git-for-windows/git/pull/1926">was optimized to become faster</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The 64-bit Portable Git <a href="https://github.com/git-for-windows/build-extra/pull/212">no longer sets <code>pack.packSizeLimit</code></a>.</li>
</ul>

</div><h2 id="v2.19.1" nr="71" class="collapsible"> Changes in v2.19.1<br /><small>since  v2.19.0 (September 11th 2018)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.19.1/Documentation/RelNotes/2.19.1.txt">Git v2.19.1</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.5.2">Git LFS v2.5.2</a>.</li>
<li>When FSCache is enabled, commands such as <code>add</code>, <code>commit</code>, and <code>reset</code> <a href="https://github.com/git-for-windows/git/pull/1827">are now much faster</a>.</li>
<li>Sublime Text, Atom, and even the new user-specific VS Code installations <a href="https://github.com/git-for-windows/build-extra/pull/200">can now be used as Git's default editor</a>.</li>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.18.0">Git Credential Manager v1.18.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Several corner case bugs <a href="https://github.com/git-for-windows/git/pull/1852">were fixed</a> in the built-in <code>rebase</code>/<code>stash</code> commands.</li>
<li>An <a href="https://github.com/git-for-windows/git/issues/1839">occasional crash in <code>git gc</code></a> (which had been introduced into v2.19.0) has been fixed.</li>
</ul>

</div><h2 id="v2.19.0" nr="72" class="collapsible"> Changes in v2.19.0<br /><small>since  v2.18.0 (June 22nd 2018)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.19.0/Documentation/RelNotes/2.19.0.txt">Git v2.19.0</a>.</li>
<li>There are now <em>fast</em>, built-in versions of <code>git stash</code> and <code>git rebase</code>, <a href="https://github.com/git-for-windows/build-extra/pull/203">available as experimental options</a>.</li>
<li>The included OpenSSH client <a href="https://github.com/git-for-windows/build-extra/pull/192">now enables modern ciphers</a>.</li>
<li>The <code>gitweb</code> component was removed because it is highly unlikely to be used on Windows.</li>
<li>The <code>git archimport</code> tool (which was probably used by exactly 0 users) is <a href="https://github.com/git-for-windows/build-extra/pull/202">no longer included in Git for Windows</a>.</li>
<li>Comes with <a href="https://github.com/jonas/tig/releases/tag/tig-2.4.0">tig v2.4.0</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.5.1">Git LFS v2.5.1</a>.</li>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.17.1">Git Credential Manager v1.17.1</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.0.2-notes.html">OpenSSL v1.0.2p</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_61_1">cURL v7.61.1</a>.</li>
<li>Comes with <a href="https://nodejs.org/en/blog/release/v8.12.0/">mingw-w64-nodejs v8.12.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The <code>http.schannel.checkRevoke</code> setting (which never worked) <a href="https://github.com/git-for-windows/git/pull/1747">was renamed to <code>http.schannelCheckRevoke</code></a>. In the same run, <code>http.schannel.useSSLCAInfo</code> (which also did not work, for the same reason) was renamed to <code>http.schannelUseSSLCAInfo</code>.</li>
<li><a href="https://github.com/git-for-windows/msys2-runtime/commit/f02cd2463d2c7e03fe97b8a1ce35ecffd0714f7e">Avoids</a> a stack overflow with recent Windows Insider versions.</li>
<li>Git GUI <a href="https://github.com/git-for-windows/git/issues/1755">now handles hooks correctly</a> in worktrees other than the main one.</li>
<li>When using <code>core.autocrlf</code>, the bogus "LF will be replaced by CRLF" warning <a href="https://github.com/git-for-windows/git/issues/1242">is now suppressed</a>.</li>
<li>The funny <a href="https://github.com/git-for-windows/git/issues/356"><code>fatal error -cmalloc would have returned NULL</code> problems</a> should be gone.</li>
</ul>

</div><h2 id="v2.18.0" nr="73" class="collapsible"> Changes in v2.18.0<br /><small>since  v2.17.1(2) (May 29th 2018)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.18.0/Documentation/RelNotes/2.18.0.txt">Git v2.18.0</a>.</li>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.16.2">Git Credential Manager v1.16.2</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The diff filter for <code>.pdf</code> files <a href="https://github.com/git-for-windows/build-extra/pull/189">was fixed</a>.</li>
<li>The <code>start-ssh-agent.cmd</code> script <a href="https://github.com/git-for-windows/MINGW-packages/pull/26">no longer overrides the <code>HOME</code> variable</a>.</li>
<li>Fixes an issue where passing an argument with a trailing slash from Git Bash to <code>git.exe</code> <a href="https://github.com/git-for-windows/git/issues/1695">was dropping that trailing slash</a>.</li>
<li>The <code>http.schannel.checkRevoke</code> setting <a href="https://github.com/git-for-windows/git/issues/1531">now really works</a>.</li>
</ul>

</div><h2 id="v2.17.1(2)" nr="74" class="collapsible"> Changes in v2.17.1(2)<br /><small>since  v2.17.1 (May 29th 2018)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.16.1">Git Credential Manager v1.16.1</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.4.2">Git LFS v2.4.2</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>This release <em>really</em> contains Git v2.17.1.</li>
</ul>

</div><h2 id="v2.17.1" nr="75" class="collapsible"> Changes in v2.17.1<br /><small>since  v2.17.0 (April 3rd 2018)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.17.1/Documentation/RelNotes/2.17.1.txt">Git v2.17.1</a>.</li>
<li>Comes with <a href="http://search.cpan.org/dist/perl-5.26.2/pod/perldelta.pod">Perl v5.26.2</a>.</li>
<li>The installer <a href="https://github.com/git-for-windows/build-extra/pull/181">now offers VS Code Insiders as option for Git's default editor</a> if it is installed.</li>
<li>The vim configuration <a href="https://github.com/git-for-windows/build-extra/pull/186">was modernized</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_60_0">cURL v7.60.0</a>.</li>
<li>Certain errors, e.g. when pushing failed due to a non-fast-forwarding change, <a href="https://github.com/git-for-windows/git/pull/1429">are now colorful</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.4.1">Git LFS v2.4.1</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Fixed an issue with recursive clone (<a href="https://aka.ms/cve-2018-11235">CVE 2018-11235</a>).</li>
<li>Aliases that expand to shell commands <a href="https://github.com/git-for-windows/git/pull/1637">can now take arguments containing curly brackets</a>.</li>
<li>Ctrl+C is now handled in Git Bash <a href="https://github.com/git-for-windows/msys2-runtime/commit/78e2deea8ec1db4aea1e78432ae98dac7198f6a5">in a sophisticated way</a>: it emulates the way Ctrl+C is handled in Git CMD, but in a fine-grained way.</li>
<li>Based on the <a href="https://github.com/git-for-windows/msys2-runtime/commit/78e2deea8ec1db4aea1e78432ae98dac7198f6a5">the new Ctrl+C handling in Git Bash</a>, pressing Ctrl+C while <code>git log</code> is running will only stop Git from traversing the commit history, <a href="https://github.com/git-for-windows/git/commit/df8884cbc5c39073848ddf2058bafeea1188312b">but keep the pager running</a>.</li>
<li>Git was <a href="https://github.com/git-for-windows/git/pull/1645">fixed</a> to work correctly in Docker volumes inside Windows containers.</li>
<li>Tab completion of <code>git status -- &lt;partial-path&gt;</code> <a href="https://github.com/git-for-windows/git/issues/1533">is now a lot faster</a>.</li>
<li>Git for Windows <a href="https://github.com/git-for-windows/git/pull/1651">now creates directory symlinks correctly</a> when asked to.</li>
<li>The option to disable revocation checks with Secure Channel which was introduced in v2.16.1(2) <a href="https://github.com/git-for-windows/git/issues/1531">now really works</a>.</li>
<li>Git <a href="https://github.com/git-for-windows/git/issues/1496">no longer enters an infinite loop</a> when misspelling <code>git status</code> as, say, <code>git Status</code>.</li>
</ul>

</div><h2 id="v2.17.0" nr="76" class="collapsible"> Changes in v2.17.0<br /><small>since  v2.16.3 (March 23rd 2018)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.17.0/Documentation/RelNotes/2.17.0.txt">Git v2.17.0</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.0.2-notes.html">OpenSSL v1.0.2o</a>.</li>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.15.2">Git Credential Manager v1.15.2</a>.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-7.7">OpenSSH v7.7p1</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>When <code>git.exe</code> is called with an invalid subcommand,  <a href="https://github.com/git-for-windows/git/issues/1591">it no longer complains about file handles</a>.</li>
</ul>

</div><h2 id="v2.16.3" nr="77" class="collapsible"> Changes in v2.16.3<br /><small>since  v2.16.2 (February 20th 2018)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.16.3/Documentation/RelNotes/2.16.3.txt">Git v2.16.3</a>.</li>
<li>When choosing to "Use Git from the Windows Command Prompt" (i.e. add only the minimal set of Git executables to the <code>PATH</code>), and when choosing the Git LFS component, Git LFS <a href="https://github.com/git-for-windows/git/issues/1503">is now included in that minimal set</a>. This makes it possible to reuse Git for Windows' Git LFS, say, from Visual Studio.</li>
<li>Comes with <a href="http://git.savannah.gnu.org/cgit/gawk.git/plain/NEWS?h=gawk-4.2.1">gawk v4.2.1</a>.</li>
<li>In conjunction with the FSCache feature, <code>git checkout</code> <a href="https://github.com/git-for-windows/git/pull/1468">is now a lot faster when checking out a <em>lot</em> of files</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.4.0">Git LFS v2.4.0</a>.</li>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.15.0">Git Credential Manager v1.15.0</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_59_0">cURL v7.59.0</a>.</li>
<li>The Git for Windows SDK <a href="https://github.com/git-for-windows/git/issues/1357">can now be "installed" via <code>git clone --depth=1 https://github.com/git-for-windows/git-sdk-64</code></a>.</li>
<li>The <code>tar</code> utility (included as a courtesy, not because Git needs it) <a href="https://github.com/git-for-windows/build-extra/pull/177">can now unpack <code>.tar.xz</code> archives</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>When a <code>TERM</code> is configured that Git for Windows does not know about, <a href="https://github.com/git-for-windows/git/issues/1473">Bash no longer crashes</a>.</li>
<li>The regression where <code>gawk</code> stopped treating Carriage Returns as part of the line endings <a href="https://github.com/git-for-windows/git/issues/1524">was fixed</a>.</li>
<li>When Git asks for credentials via the terminal in a Powershell window, <a href="https://github.com/git-for-windows/git/pull/1514">it no longer fails to do so</a>.</li>
<li>The installer <a href="https://github.com/git-for-windows/build-extra/commit/d33ee8606bfbc0e9b801df0a5257721e20f8dd4a">is now more robust when encountering files that are in use</a> (and can therefore not be overwritten right away).</li>
<li>The included <code>find</code> and <code>rm</code> utilities <a href="https://github.com/git-for-windows/git/issues/1497">no longer have problems with deeply nested directories on FAT drives</a>.</li>
<li>The <code>cygpath</code> utility included in Git for Windows now strips trailing slashes when normalizing paths (just like the Cygwin version of the utility; this is <em>different</em> from how MSYS2 chooses to do things).</li>
<li>The certificates of HTTPS proxies configured via <code>http.proxy</code> <a href="https://github.com/git-for-windows/git/issues/1493">are now validated against the <code>ca-bundle.crt</code> correctly</a>.</li>
</ul>

</div><h2 id="v2.16.2" nr="78" class="collapsible"> Changes in v2.16.2<br /><small>since  v2.16.1(4) (February 7th 2018)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.16.2/Documentation/RelNotes/2.16.2.txt">Git v2.16.2</a>.</li>
<li>For every new Git for Windows version, <code>.zip</code> archives containing <code>.pdb</code> files for some of Git for Windows' components <a href="https://github.com/git-for-windows/build-extra/commit/0af1701ba3329151ae8b21fa43d4f4abca11cc26">are now published alongside the new version</a>.</li>
<li>Comes with MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/ml/cygwin-announce/2018-02/msg00002.html">Cygwin 2.10.0</a>; This required rebuilding OpenSSH, Perl (and some Perl modules) and Subversion.</li>
<li>Comes with <a href="https://tiswww.case.edu/php/chet/bash/NEWS">Bash v4.4 patchlevel 019 </a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The Perl upgrade in Git for Windows v2.16.1(4) <a href="https://github.com/git-for-windows/git/issues/1488">broke interactive authentication of <code>git svn</code></a>, which was fixed.</li>
<li>When configuring HTTPS transport to use Secure Channel, <a href="https://github.com/git-for-windows/build-extra/pull/172">we now refrain from configuring <code>http.sslCAInfo</code></a>. This also helps Git LFS (which uses Git for Windows' private <code>http.sslCAInfo</code> setting) to use the same credentials as <code>git fetch</code> and <code>git push</code>.</li>
</ul>

</div><h2 id="v2.16.1(4)" nr="79" class="collapsible"> Changes in v2.16.1(4)<br /><small>since  v2.16.1(3) (February 6th 2018)</h2></small><div>

<h3>Bug Fixes</h3>

<ul>
<li>When called from TortoiseGit, <code>git.exe</code> <a href="https://github.com/git-for-windows/git/issues/1481">can now spawn processes again</a>.</li>
</ul>

</div><h2 id="v2.16.1(3)" nr="80" class="collapsible"> Changes in v2.16.1(3)<br /><small>since  v2.16.1(2) (February 2nd 2018)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Git for Windows' SDK packages <a href="https://github.com/git-for-windows/build-extra/commit/53695c41ec95f49c191b7792eee6fc8d91846ed8">are now hosted on Azure Blobs</a>, fixing part of <a href="https://github.com/git-for-windows/git/issues/1479">issue #1479</a>.</li>
<li>Comes with <a href="https://metacpan.org/source/MIKEM/Net-SSLeay-1.84/Changes">perl-Net-SSLeay v1.84</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>When <code>http.sslBackend</code> is not configured (e.g. in portable Git or MinGit), fetch/push operations <a href="https://github.com/git-for-windows/git/issues/1474">no longer crash</a>.</li>
<li>On Windows 7 and older, Git for Windows v2.16.1(2) was no longer able to spawn any processes (e.g. during fetch/clone). This regression <a href="https://github.com/git-for-windows/git/issues/1475">has been fixed</a>.</li>
<li>The Perl upgrade in v2.16.1(2) broke <code>git send-email</code>; This <a href="https://github.com/git-for-windows/git/issues/1480">has been fixed</a> by updating the Net-SSLeay Perl module.</li>
</ul>

</div><h2 id="v2.16.1(2)" nr="81" class="collapsible"> Changes in v2.16.1(2)<br /><small>since  v2.16.1 (January 22nd 2018)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="http://h5l.org/releases.html">Heimdal v7.5.0</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_58_0">cURL v7.58.0</a>.</li>
<li>Comes with <a href="http://search.cpan.org/dist/perl-5.26.1/pod/perldelta.pod">Perl v5.26.1</a>.</li>
<li>When using GNU nano as Git's default editor, <a href="https://github.com/git-for-windows/build-extra/pull/169">it is now colorful (shows syntax-highlighting)</a>.</li>
<li>Comes with <a href="https://github.com/jonas/tig/releases/tag/tig-2.3.3">tig v2.3.3</a>.</li>
<li>When using Secure Channel as HTTPS transport behind a proxy, it may be necessary to disable revocation checks, <a href="https://github.com/git-for-windows/git/pull/1450">which is now possible</a>.</li>
<li>Comes with <a href="https://github.com/git-for-windows/busybox-w32/commit/0b3cdd76c">BusyBox v1.28.0pre.16550.0b3cdd76c</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>When Git spawns processes, <a href="https://github.com/git-for-windows/git/commit/576ff26eeca22526b7ba11444da24d31daf0b369">now only the necessary file handles are inherited from the parent process</a>, possibly preventing file locking issues.</li>
<li>The <code>git update</code> command <a href="https://github.com/git-for-windows/build-extra/pull/167">has been renamed to <code>git update-git-for-windows</code></a> to avoid confusion where users may think that <code>git update</code> updates their local repository or worktree.</li>
</ul>

</div><h2 id="v2.16.1" nr="82" class="collapsible"> Changes in v2.16.1<br /><small>since  v2.16.0(2) (January 18th 2018)</h2></small><div>

<p>This is a hotfix release, based on upstream Git's hotfix to address a possible segmentation fault associated with case-insensitive file systems.</p>

<p>Note: another hotfix might be coming the day after tomorrow, as cURL announced a new version addressing security advisories that <em>might</em> affect how Git talks via HTTP/HTTPS, too.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.16.1/Documentation/RelNotes/2.16.1.txt">Git v2.16.1</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>A set of regressions introduced by patches intended to speed up <code>reset</code> and <code>checkout</code> was fixed (issues <a href="https://github.com/git-for-windows/git/issues/1437">#1437</a>, <a href="https://github.com/git-for-windows/git/issues/1438">#1438</a>, <a href="https://github.com/git-for-windows/git/issues/1440">#1440</a> and <a href="https://github.com/git-for-windows/git/issues/1442">#1442</a>).</li>
</ul>

</div><h2 id="v2.16.0(2)" nr="83" class="collapsible"> Changes in v2.16.0(2)<br /><small>since  v2.15.1(2) (November 30th 2017)</h2></small><div>

<p>Git for Windows now has a new homepage: <a href="https://gitforwindows.org/">https://gitforwindows.org/</a> (it is still graciously hosted by GitHub, but now much quicker to type).</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.16.0/Documentation/RelNotes/2.16.0.txt">Git v2.16.0</a>.</li>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.14.0">Git Credential Manager v1.14.0</a>.</li>
<li>The Git for Windows installer <a href="https://github.com/git-for-windows/git/issues/1356">now offers to configure Visual Studio Code as default editor for Git</a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/openssl-1.0.2-notes.html">OpenSSL v1.0.2n</a>.</li>
<li><code>git checkout</code> <a href="https://github.com/git-for-windows/git/pull/1419">is now a lot faster when checking out a <em>lot</em> of files</a>.</li>
<li>The <code>core.excludesfile</code> <a href="https://github.com/git-for-windows/git/issues/1392">can now reference a symbolic link</a>.</li>
<li>Comes with <a href="https://github.com/git-for-windows/msys2-runtime/commit/c967bd8e37af7fa86f8ed1ded2625071612b808a">patch level 7</a> of the MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/ml/cygwin-announce/2017-09/msg00056.html">Cygwin 2.9.0</a>.</li>
<li>With lots of files, <code>git reset --hard</code> <a href="https://github.com/git-for-windows/git/pull/1427">is now a lot faster</a> when the FSCache feature is in effect.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>When cloning into an existing (empty) directory fails, <a href="https://github.com/git-for-windows/git/pull/1421">Git no longer removes said directory</a>.</li>
<li>Interrupting processes (and their children) using Control+C <a href="https://github.com/git-for-windows/msys2-runtime/pull/16">is now a lot more robust</a>.</li>
</ul>

</div><h2 id="v2.15.1(2)" nr="84" class="collapsible"> Changes in v2.15.1(2)<br /><small>since  v2.15.1 (November 29th 2017)</h2></small><div>

<h3>Bug Fixes</h3>

<ul>
<li>The bug introduced into Git for Windows v2.15.1 where <code>vim</code> would show an ugly warning upon startup <a href="https://github.com/git-for-windows/git/issues/1382">was fixed</a>.</li>
</ul>

</div><h2 id="v2.15.1" nr="85" class="collapsible"> Changes in v2.15.1<br /><small>since  v2.15.0 (October 30th 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.15.1/Documentation/RelNotes/2.15.1.txt">Git v2.15.1</a>.</li>
<li>Operations in massively-sparse worktrees <a href="https://github.com/git-for-windows/git/pull/1344">are now much faster if <code>core.fscache = true</code></a>.</li>
<li>It is <a href="https://github.com/git-for-windows/build-extra/pull/161">now possible to configure <code>nano</code></a> or <a href="https://github.com/git-for-windows/git/issues/291">Notepad++</a> as Git's default editor <a href="https://www.xkcd.com/378/">instead of <code>vim</code></a>.</li>
<li>Comes with <a href="https://www.openssl.org/news/cl102.txt">OpenSSL v1.0.2m</a>.</li>
<li>Git for Windows' updater <a href="https://github.com/git-for-windows/build-extra/commit/ab2e8b1ee14223dbfdc7981e79139727d0725e7c">now uses non-intrusive toast notifications on Windows 8, 8.1 and 10</a>.</li>
<li>Running <code>git fetch</code> in a repository with lots of refs <a href="https://github.com/git-for-windows/git/pull/1379">is now considerably faster</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_57_0">cURL v7.57.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The experimental <code>--show-ignored-directory</code> option of <code>git status</code> which was removed in Git for Windows v2.15.0 without warning <a href="https://github.com/git-for-windows/git/pull/1354">has been reintroduced as a deprecated option</a>.</li>
<li>The <code>git update</code> command (to auto-update Git for Windows) will <a href="https://github.com/git-for-windows/git/issues/1363">now also work behind proxies</a>.</li>
</ul>

</div><h2 id="v2.15.0" nr="86" class="collapsible"> Changes in v2.15.0<br /><small>since  v2.14.3 (October 23rd 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.15.0/Documentation/RelNotes/2.15.0.txt">Git v2.15.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The auto-updater tried to run at a precise time, and did not run when the computer was switched off at that time. <a href="https://github.com/git-for-windows/build-extra/commit/459b6e85c">Now it runs as soon after the scheduled time as possible</a>.</li>
<li>The auto-updater <a href="https://github.com/git-for-windows/build-extra/commit/1418ee7e8">no longer suggests to downgrade from Release Candidates</a>.</li>
<li>When the auto-updater asked the user whether they want to upgrade to a certain version, and the user declined, <a href="https://github.com/git-for-windows/build-extra/commit/c0f7634af">the auto-updater will not bother the user about said version again</a>.</li>
<li>The installer, when run with /SKIPIFINUSE=1, <a href="https://github.com/git-for-windows/build-extra/commit/db3521c140154b3923e304e4271176958da1f048">now detects whether <em>any</em> executable in Git for Windows' installation is run</a></li>
<li>Git for Windows <a href="https://github.com/git-for-windows/build-extra/commit/c86d164f2c9d5c79cd95f1fda881f9e80ca9dc3a">no longer includes (non-working) <code>xmlcatalog.exe</code> and <code>xmllint.exe</code></a>.</li>
</ul>

</div><h2 id="v2.14.3" nr="87" class="collapsible"> Changes in v2.14.3<br /><small>since  v2.14.2(3) (October 12th 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.14.3/Documentation/RelNotes/2.14.3.txt">Git v2.14.3</a>.</li>
<li>Git for Windows <a href="https://github.com/git-for-windows/build-extra/pull/148">now ships with a diff helper for OpenOffice documents</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.3.4">Git LFS v2.3.4</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_56_1">cURL v7.56.1</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git for Windows <a href="https://github.com/git-for-windows/git/issues/1320">now handles worktrees at the top-level of a UNC share correctly</a>.</li>
</ul>

</div><h2 id="v2.14.2(3)" nr="88" class="collapsible"> Changes in v2.14.2(3)<br /><small>since  v2.14.2(2) (October 5th 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.3.3">Git LFS v2.3.3</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li><a href="https://github.com/git-for-windows/build-extra/commit/b46fba6f44b3680210b19ef5fc9ce22ca1dcda55">Re-enabled some SSHv1 ciphers</a> since some sites (e.g. Visual Studio Team Services) rely on them for the time being.</li>
</ul>

</div><h2 id="v2.14.2(2)" nr="89" class="collapsible"> Changes in v2.14.2(2)<br /><small>since  v2.14.2 (September 26th 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git-for-windows/busybox-w32/commit/b4c390e17">BusyBox v1.28.0pre.16467.b4c390e17</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.3.2">Git LFS v2.3.2</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_56_0">cURL v7.56.0</a>.</li>
<li>Comes with <a href="https://www.openssh.com/txt/release-7.6">OpenSSH v7.6p1</a>.</li>
<li>Comes with <a href="https://github.com/git-for-windows/MSYS2-packages/commit/f2caef90d2e6ba13dc16e38152003958f4db710b">patch level 4</a> of the MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/ml/cygwin-announce/2017-09/msg00056.html">Cygwin 2.9.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>A <a href="https://github.com/git-for-windows/git/issues/1312">bug</a> which caused the console window to be closed when executing certain Bash scripts <a href="https://github.com/git-for-windows/MSYS2-packages/commit/e9d0a2be2720007c2a734866ebbb4c15e503003c">was fixed</a>.</li>
<li>A crash when calling <code>kill &lt;pid&gt;</code> for a non-existing process <a href="https://github.com/git-for-windows/git/issues/1316">was fixed</a>.</li>
</ul>

</div><h2 id="v2.14.2" nr="90" class="collapsible"> Changes in v2.14.2<br /><small>since  v2.14.1 (August 10th 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.14.2/Documentation/RelNotes/2.14.2.txt">Git v2.14.2</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_55_1">cURL v7.55.1</a>.</li>
<li>The XP-compatibility layer emulating pthreads (which is <a href="https://git-for-windows.github.io/requirements.html">no longer needed</a>) <a href="https://github.com/git-for-windows/git/pull/1214">was dropped in favor of modern Windows threading APIs</a>; This should make threaded operations slightly faster and more robust.</li>
<li>On Windows, UNC paths can <a href="https://github.com/git-for-windows/git/commit/a352941117bc8d00dfddd7a594adf095d084d844">now be accessed via <code>file://host/share/repo.git</code>-style paths</a>.</li>
<li>Comes with <a href="https://github.com/git-for-windows/build-extra/pull/151">a new custom Git command <code>git update</code></a> to help keeping Git up-to-date on your machine.</li>
<li>The Git installer now offers <a href="https://github.com/git-for-windows/build-extra/pull/155">an option to keep Git up-to-date</a> by calling <code>git update</code> regularly.</li>
<li>Comes with <a href="https://github.com/git-for-windows/busybox-w32/commit/2739df917">BusyBox v1.28.0pre.16353.2739df917</a>.</li>
<li>As is common elsewhere, Ctrl+Left and Ctrl+Right <a href="https://github.com/git-for-windows/build-extra/pull/156">now move word-wise in Git Bash</a>, too.</li>
<li>Comes with <a href="https://github.com/git-for-windows/msys2-runtime/commit/874e2c8efeed9084cd065cf9ea5c0951f5afca02">patch level 2</a> of the MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/ml/cygwin-announce/2017-09/msg00056.html">Cygwin 2.9.0</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.3.0">Git LFS v2.3.0</a>.</li>
<li>The <code>vs/master</code> branch <a href="https://github.com/git-for-windows/git/pull/1302">can now be built in Visual Studio 2017</a>, too</li>
<li>As <a href="https://github.com/git-for-windows/git/issues/1294">requested</a> by the same user who implemented <a href="https://github.com/git-for-windows/build-extra/pull/157">the change</a>, Git for Windows now comes with <a href="https://github.com/jonas/tig"><code>tig</code></a>, a text-mode interface for Git.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>It is <a href="https://github.com/git-for-windows/git/commit/70c1ff8b0ef66321d630fe49d61ee1a9b6be6a4c">now possible to override <code>http.sslBackend</code> on the command-line</a>.</li>
<li>The installer <a href="https://github.com/git-for-windows/build-extra/commit/5e438f707027eb99da1b1b381672e6d7dbc063a8">now detects correctly whether symbolic links can be created by regular users</a>.</li>
<li>Git Bash <a href="https://github.com/git-for-windows/build-extra/pull/152">now renders non-ASCII directories nicely</a>.</li>
<li>A regression that caused the fetch operation with lots of refs to be a lot slower than before <a href="https://github.com/git-for-windows/git/issues/1233">was fixed</a>.</li>
<li>The <code>git-gui.exe</code> and <code>gitk.exe</code> wrappers intended to be used in Git CMD <a href="https://github.com/git-for-windows/git/issues/1284">now handle command-line parameters correctly</a>.</li>
<li>The <code>core.longPaths</code> setting <a href="https://github.com/git-for-windows/git/issues/1218">is now heeded when packing refs</a>, and other previously forgotten Git commands.</li>
<li>Pressing Ctrl+Z in Git Bash <a href="https://github.com/git-for-windows/git/issues/1083">no longer kills Win32 processes (e.g. <code>git.exe</code>) anymore</a>, because POSIX job control is only available with MSYS2 processes.</li>
<li>Git for Windows <a href="https://github.com/git-for-windows/git/commit/b5915c6ae881518927b9fa0b3c4df4d3edd37f23">now sets <code>core.fsyncObjectFiles = true</code> by default</a> which makes it a lot more fault-tolerant, say, when power is lost.</li>
<li>A bug has been fixed where Git for Windows <a href="https://github.com/git-for-windows/git/issues/1299">could run into an infinite loop trying to rename a file</a>.</li>
<li>Before installing Git for Windows, we already verified that no Git Bash instance is active (which would prevent files from being overwritten). We <a href="https://github.com/git-for-windows/build-extra/commit/1b93b50cf08c6cbd3200a66603d28fbd269c2f6a">now also verify that no <code>git.exe</code> processes are active, either</a>.</li>
</ul>

</div><h2 id="v2.14.1" nr="91" class="collapsible"> Changes in v2.14.1<br /><small>since  v2.14.0(2) (August 7th 2017)</h2></small><div>

<p>Note: there have been MinGit-only releases v2.12.2(3) and v2.13.1(3) with backports of the important bug fix in v2.14.1 as well as the experimental <code>--show-ignored-directory</code> option of <code>git status</code>.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.14.1/Documentation/RelNotes/2.14.1.txt">Git v2.14.1</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_55_0">cURL v7.55.0</a>.</li>
<li>The <em>Git Bash Here</em> context menu item <a href="https://github.com/git-for-windows/build-extra/pull/150">is now also available</a> in the special <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/dd758096.aspx">Libraries folders</a>.</li>
</ul>

</div><h2 id="v2.14.0(2)" nr="92" class="collapsible"> Changes in v2.14.0(2)<br /><small>since  v2.14.0 (August 6th 2017)</h2></small><div>

<h3>Bug Fixes</h3>

<ul>
<li>A regression introduced in v2.14.0 that prevented fetching via SSH <a href="https://github.com/git-for-windows/git/issues/1258">was fixed</a>.</li>
</ul>

</div><h2 id="v2.14.0" nr="93" class="collapsible"> Changes in v2.14.0<br /><small>since  v2.13.3 (July 13th 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.14.0/Documentation/RelNotes/2.14.0.txt">Git v2.14.0</a>.</li>
<li>Comes with <a href="https://github.com/git-for-windows/busybox-w32/commit/9480dca7c">BusyBox v1.28.0pre.15857.9480dca7c</a>.</li>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.12.0">Git Credential Manager v1.12.0</a>.</li>
<li>It is now possible to switch between Secure Channel and OpenSSL for Git's HTTPS transport by <a href="https://github.com/git-for-windows/git/commit/d81216ee4dd46ae59a388044d1266d6fa9030c19">setting the <code>http.sslBackend</code> config variable to "openssl" or "schannel"</a>; This <a href="https://github.com/git-for-windows/build-extra/commit/7c5a23970126e3cff1e1a7a763216b2a67005593">is now also the method used by the installer</a> (rather than copying <code>libcurl-4.dll</code> files around).</li>
<li>The experimental option <a href="https://github.com/git-for-windows/git/pull/1243"><code>--show-ignored-directory</code> was added to <code>git status</code></a> to show only the name of ignored directories when the option <code>--untracked=all</code> is used.</li>
<li>Git for Windows releases now also include an experimental <a href="https://github.com/git-for-windows/git/wiki/MinGit#experimental-busybox-based-mingit">BusyBox-based MinGit</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Repository-local aliases <a href="https://github.com/git-for-windows/git/commit/6ba04141d88">are now resolved again in worktrees</a>.</li>
<li>CamelCased aliases were broken in v2.13.3; This <a href="https://github.com/git-for-windows/git/commit/af0c2223da0">has been fixed again</a>.</li>
<li>The 32-bit Git binaries are now built against the same dependencies that are shipped with Git for Windows.</li>
</ul>

</div><h2 id="v2.13.3" nr="94" class="collapsible"> Changes in v2.13.3<br /><small>since  v2.13.2 (June 26th 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.13.3/Documentation/RelNotes/2.13.3.txt">Git v2.13.3</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.2.1">Git LFS v2.2.1</a>.</li>
<li>Comes with MSYS2 runtime (Git for Windows flavor) based on <a href="https://cygwin.com/ml/cygwin-announce/2017-07/msg00044.html">Cygwin 2.8.2</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git Bash <a href="https://github.com/git-for-windows/git/issues/1226">no longer tries to use the <code>getent</code> tool</a> which was never shipped with Git for Windows.</li>
</ul>

</div><h2 id="v2.13.2" nr="95" class="collapsible"> Changes in v2.13.2<br /><small>since  v2.13.1(2) (June 15th 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.13.2/Documentation/RelNotes/2.13.2.txt">Git v2.13.2</a>.</li>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.10.1">Git Credential Manager v1.10.1</a>.</li>
<li>The Git Bash prompt <a href="https://github.com/git-for-windows/build-extra/pull/145">can now be overridden by creating the file <code>.config\git\git-prompt.sh</code></a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html#7_54_1">cURL v7.54.1</a>.</li>
</ul>

</div><h2 id="v2.13.1(2)" nr="96" class="collapsible"> Changes in v2.13.1(2)<br /><small>since  v2.13.1 (June 13th 2017)</h2></small><div>

<h3>Bug Fixes</h3>

<ul>
<li><code>git commit</code> and <code>git status</code> <a href="https://github.com/git-for-windows/git/issues/1202">no longer randomly throw segmentation faults</a>.</li>
</ul>

</div><h2 id="v2.13.1" nr="97" class="collapsible"> Changes in v2.13.1<br /><small>since  v2.13.0 (May 10th 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.13.1/Documentation/RelNotes/2.13.1.txt">Git v2.13.1</a>.</li>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.10.0">Git Credential Manager v1.10.0</a>.</li>
<li>Comes with <a href="https://www.openssh.com/releasenotes.html#7.5p1">OpenSSH 7.5p1</a>.</li>
<li>Comes with <a href="https://github.com/petervanderdoes/gitflow-avh/releases/tag/1.11.0">Git Flow v1.11.0</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.1.1">Git LFS v2.1.1</a>.</li>
<li>Git <a href="https://github.com/git-for-windows/git/pull/1188">now uses the flag introduced with Windows 10 Creators Update to create symbolic links without requiring elevated privileges</a> in Developer Mode.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The documentation of Git for Windows' several config files <a href="https://github.com/git-for-windows/git/pull/1165">was improved</a>.</li>
<li>When interrupting Git processes in Git Bash by pressing Ctrl+C, <a href="https://github.com/git-for-windows/msys2-runtime/pull/15">Git now removes <code>.lock</code> files as designed</a> (<a href="https://github.com/git-for-windows/git/pull/1170">accompanying Git PR</a>; this should also fix <a href="https://github.com/git-for-windows/git/issues/338">issue #338</a>).</li>
<li><code>git status -uno</code> <a href="https://github.com/git-for-windows/git/issues/1179">now treats submodules in ignored directories correctly</a>.</li>
<li>The fscache feature <a href="https://github.com/git-for-windows/git/commit/bda7f0728ac55e55d79ed0786c1b5ce2ef7e6117">no longer slows down <code>git commit -m &lt;message&gt;</code> in large worktrees</a>.</li>
<li>Executing <code>git.exe</code> in Git Bash when the current working directory is a UNC path <a href="https://github.com/git-for-windows/git/issues/1181">now works as expected</a>.</li>
<li>Staging/unstaging multiple files in Git GUI via Ctrl+C <a href="https://github.com/git-for-windows/git/issues/1012">now works</a>.</li>
<li>When hitting Ctrl+T in Git GUI to stage files, but the file list is empty, Git GUI <a href="https://github.com/git-for-windows/git/issues/1075">no longer shows an exception window</a>.</li>
</ul>

</div><h2 id="v2.13.0" nr="98" class="collapsible"> Changes in v2.13.0<br /><small>since  v2.12.2(2) (April 5th 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.13.0/Documentation/RelNotes/2.13.0.txt">Git v2.13.0</a>.</li>
<li>Comes with <a href="https://curl.haxx.se/changes.html">cURL v7.54.0</a>.</li>
<li>Comes with <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.1.0">Git LFS v2.1.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>As per Git LFS' convention, <a href="https://github.com/git-for-windows/build-extra/pull/141">it is installed into the <code>bin/</code> directory again</a>.</li>
<li>Calling <code>git add</code> with an absolute path using different upper/lower case than recorded on disk <a href="https://github.com/git-for-windows/git/issues/735">will now work as expected</a> instead of claiming that the paths are outside the repository.</li>
<li>Git for Windows <a href="https://github.com/git-for-windows/git/issues/1150">no longer tries to determine the default printer</a>.</li>
<li>When writing the Git index file, Git for Windows <a href="https://github.com/git-for-windows/git/issues/1149">no longer has the wrong idea about the file's timestamp</a>.</li>
<li>On Windows, absolute paths can start with a backslash (implicitly referring to the same drive as the current directory), and now <code>git clone</code> <a href="https://github.com/git-for-windows/git/commit/fad23e90efc">can use those paths, too</a>.</li>
</ul>

</div><h2 id="v2.12.2(2)" nr="99" class="collapsible"> Changes in v2.12.2(2)<br /><small>since  v2.12.2 (March 27th 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Portable Git is now using <a href="https://github.com/git-for-windows/7-Zip">a custom-built SFX that is based directly on 7-Zip's SFX</a>.</li>
<li>Git LFS was upgraded to <a href="https://github.com/git-lfs/git-lfs/releases/tag/v2.0.2">v2.0.2</a>.</li>
<li>Updated the MSYS2 runtime to <a href="https://cygwin.com/ml/cygwin-announce/2017-04/msg00001.html">Cygwin 2.8.0</a>.</li>
<li>Git LFS <a href="https://github.com/git-for-windows/build-extra/commit/16975a72fd328130ae531ce349e4a77d9d2b8fa4">can now be disabled in the first installer page</a> (users can still enable it manually, as before, of course).</li>
<li>Comes with <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/">Git Credential Manager</a> v1.9.1.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>A potential crash in <code>git status</code> with lots of files <a href="https://github.com/git-for-windows/git/issues/1111">was fixed</a>.</li>
<li>Git LFS <a href="https://github.com/git-for-windows/build-extra/commit/5f7d44728c089694f4ef1cc3da03f15e35cd5ecc">now gets installed into the correct location</a>.</li>
<li>Git LFS <a href="https://github.com/git-for-windows/build-extra/commit/115b9f5b88ff60af19628262833b42cd7b6cd852">is now configured correctly out of the box</a> (unless disabled).</li>
<li>The <code>http.sslCAInfo</code> config setting <a href="https://github.com/git-for-windows/git/issues/531">is now private to the Git for Windows installation that owns the file</a>.</li>
<li><code>git difftool -d</code> <a href="https://github.com/git-for-windows/git/issues/1124">no longer crashes randomly</a>.</li>
</ul>

</div><h2 id="v2.12.2" nr="100" class="collapsible"> Changes in v2.12.2<br /><small>since  v2.12.1 (March 21st 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.12.2/Documentation/RelNotes/2.12.2.txt">Git v2.12.2</a>.</li>
<li>An earlier iteration of the changes speeding up the case-insensitive cache of file names was replaced by <a href="https://github.com/git-for-windows/git/commit/212247dd6345c820deeae61fcdf2f10cea10525a">a new iteration</a>.</li>
</ul>

</div><h2 id="v2.12.1" nr="101" class="collapsible"> Changes in v2.12.1<br /><small>since  v2.12.0 (February 25th 2017)</h2></small><div>

<p>A <a href="https://github.com/git-for-windows/git/releases/tag/v2.12.0.windows.2">MinGit-only v2.12.0(2)</a> was released in the meantime.</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.12.1/Documentation/RelNotes/2.12.1.txt">Git v2.12.1</a>.</li>
<li>In addition to the GitForWindows NuGet package, we now also publish <a href="https://www.nuget.org/packages/Git-Windows-Minimal/">MinGit as a NuGet package</a>.</li>
<li>Git for Windows now bundles <a href="https://git-lfs.github.com/">Git LFS</a>.</li>
<li>Comes with Git Credential Manager <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.9.0">v1.9.0</a>.</li>
<li>Git can now be configured to use <a href="https://github.com/git-for-windows/git/issues/301">Secure Channel</a> to use the Windows Credential Store when fetching/pushing via HTTPS.</li>
<li><a href="https://github.com/git-for-windows/MSYS2-packages/pull/20">Updates</a> Git-Flow to <a href="https://github.com/petervanderdoes/gitflow-avh/blob/1.10.2/Changes.mdown#1102">v1.10.2</a> (addressing <a href="https://github.com/git-for-windows/git/issues/1092">#1092</a>).</li>
<li>Git for Windows' fork of the MSYS2 runtime was <a href="https://github.com/git-for-windows/msys2-runtime/compare/5f79e89da8...a55abf375d">rebased</a> to a preview of the Cygwin runtime version 2.8.0 (due soon) to fix <a href="https://cygwin.com/ml/cygwin/2017-03/msg00113.html"><code>fork: child &lt;n&gt; - forked process &lt;pid&gt; died unexpectedly, retry 0, exit code 0xC0000142, errno 11</code> problems</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>MinGit <a href="https://github.com/git-for-windows/git/issues/1086">no longer gets distracted</a> by incompatible <code>libeay32.dll</code> versions in C:\Windows\system32.</li>
<li>Long paths between 248 and 260 characters were not handled correctly since Git for Windows v2.11.1, which <a href="https://github.com/git-for-windows/git/issues/1084">is now fixed</a>.</li>
<li>The <code>awk.exe</code> shipped with MinGit <a href="https://github.com/git-for-windows/build-extra/commit/437b52cae9d73772f9582efbd45b63335c7a3fb8">now ships with a previously missing a dependency</a> (this fixes <code>git mergetool</code>).</li>
<li>Git for Windows does not ship with localized messages to save on bandwidth, and the gettext initialization <a href="https://github.com/git-for-windows/git/commit/0a416e8f3ef5314927f687f8b2e90f68bc537d80">can be skipped when the directory with said messages is missing</a>, saving us up to 150ms on every <code>git.exe</code> startup.</li>
<li>A possible crash when running <code>git log --pickaxe-regex -S&lt;regex&gt;</code> <a href="https://github.com/git-for-windows/git/commit/2c6cf4e358dd1395091e1d7f9544028e6df674a7">was fixed</a>.</li>
<li>The <code>ORIGINAL_PATH</code> variable, recently introduced by the MSYS2 project to allow for special "PATH modes", <a href="https://github.com/git-for-windows/msys2-runtime/commit/476605ced959f217b3820157b8101b4529fa6a0d">is now handled in the same manner as the <code>PATH</code> variable</a> when jumping the Windows&lt;->MSYS2 boundary, fixing issues when <code>ORIGINAL_PATH</code> is converted to Windows format and back again.</li>
</ul>

</div><h2 id="v2.12.0" nr="102" class="collapsible"> Changes in v2.12.0<br /><small>since  v2.11.1 (February 3rd 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.12.0/Documentation/RelNotes/2.12.0.txt">Git v2.12.0</a>.</li>
<li>The builtin difftool is no longer opt-in, as it graduated to be officially adopted by the Git project.</li>
<li>Comes with v2.7.0 of the POSIX emulation layer based on the <a href="https://cygwin.com/ml/cygwin-announce/2017-02/msg00022.html">Cygwin runtime</a>.</li>
<li>Includes <a href="https://curl.haxx.se/changes.html#7_53_1">cURL 7.53.1</a>.</li>
<li>The Portable Git now defaults to using the included Git Credential Manager.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The <a href="https://github.com/git-for-windows/git/commit/87ad093f001e7146e5e521914255199e49c212a7"><code>stderr</code> output is unbuffered again</a>, i.e. errors are displayed immediately (this was reported <a href="http://public-inbox.org/git/6bc02b0a-a463-1f0c-3fee-ba27dd2482e4@kdbg.org/">on the Git mailing list</a> as well as issues <a href="https://github.com/git-for-windows/git/issues/1062">#1064</a>, <a href="https://github.com/git-for-windows/git/issues/1064">#1064</a>, <a href="https://github.com/git-for-windows/git/issues/1068">#1068</a>).</li>
<li>Git <a href="https://github.com/git-for-windows/git/issues/1036">can clone again</a> from paths containing non-ASCII characters.</li>
<li>We <a href="https://github.com/git-for-windows/git/issues/1069">no longer ship two different versions of <code>curl.exe</code></a>.</li>
<li>Hitting Ctrl+T in Git GUI even after all files have been (un)staged <a href="https://github.com/git-for-windows/git/issues/1060">no longer throws an exception</a>.</li>
<li>A couple of Git GUI bugs regarding the list of recent repositories <a href="https://github.com/patthoyts/git-gui/pull/10">have been fixed</a>.</li>
<li>The <code>git-bash.exe</code> helper <a href="https://github.com/git-for-windows/git/issues/946">now waits again for the terminal to be closed before returning</a>.</li>
<li>Git for Windows <a href="https://github.com/git-for-windows/git/issues/1034">no longer attempts to send empty credentials to HTTP(S) servers that handle only Basic and/or Digest authentication</a>.</li>
</ul>

</div><h2 id="v2.11.1" nr="103" class="collapsible"> Changes in v2.11.1<br /><small>since  v2.11.0(3) (January 14th 2017)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.11.1/Documentation/RelNotes/2.11.1.txt">Git v2.11.1</a>.</li>
<li>Performance <a href="https://github.com/git-for-windows/git/pull/994">was enhanced when using fscache in a massively sparse checkout</a>.</li>
<li>Git hooks <a href="https://github.com/git-for-windows/git/commit/1c6c2420ff6683d93a61fc790842ab712f2a926b">can now be <code>.exe</code> files</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git GUI will <a href="https://github.com/git-for-windows/git/pull/1032">no longer set <code>GIT_DIR</code> when calling Git Bash after visualizing the commit history</a>.</li>
<li>When the <code>PATH</code> contains UNC entries, Git Bash will <a href="https://github.com/git-for-windows/git/issues/1033">no longer error out with a "Bad address" error message</a>.</li>
</ul>

</div><h2 id="v2.11.0(3)" nr="104" class="collapsible"> Changes in v2.11.0(3)<br /><small>since  v2.11.0(2) (January 13th 2017)</h2></small><div>

<h3>Bug Fixes</h3>

<ul>
<li><a href="https://github.com/git-for-windows/msys2-runtime/commit/cfaf466391f992525a66d91ebb8e33cadbc08438">Fixed an off-by-two bug in the POSIX emulation layer</a> that possibly affected third-party Perl scripts that load native libraries dynamically.</li>
<li>A regression in <code>rebase -i</code>, introduced into v2.11.0(2), which caused commit attribution to be mishandled after resolving conflicts, <a href="https://github.com/git-for-windows/git/commit/e11df2efb3072fe73153442589129d2eb8d9ea02">was fixed</a>.</li>
</ul>

</div><h2 id="v2.11.0(2)" nr="105" class="collapsible"> Changes in v2.11.0(2)<br /><small>since  v2.11.0 (December 1st 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Reading a large index <a href="https://github.com/git-for-windows/git/pull/978">has been speeded up using pthreads</a>.</li>
<li>The <code>checkout</code> operation <a href="https://github.com/git-for-windows/git/pull/988">was speeded up</a> for the common cases.</li>
<li>The <code>status</code> operation <a href="https://github.com/git-for-windows/git/pull/991">was made faster</a> in large worktrees with many changes.</li>
<li>The <code>diff</code> operation saw <a href="https://github.com/git-for-windows/git/pull/996">performance improvements</a> when working on a huge number of renamed files.</li>
<li>PuTTY's <code>plink.exe</code> <a href="https://github.com/git-for-windows/git/pull/1006">can now be used in <code>GIT_SSH_COMMAND</code> without jumping through hoops, too</a>.</li>
<li>The MSYS2 runtime was <a href="https://github.com/git-for-windows/msys2-runtime/commit/038b376b2b02ab916eabac006ac54b1d29a4be75">synchronized with Cygwin 2.6.1</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Non-ASCII characters are <a href="https://github.com/git-for-windows/git/issues/981">now shown properly again</a> in Git Bash.</li>
<li>Implicit NTLM authentication <a href="https://github.com/git-for-windows/git/issues/987">works again</a> when accessing a remote repository via HTTP/HTTPS without having to specify empty user name and password.</li>
<li>Our <code>poll()</code> emulation <a href="https://github.com/git-for-windows/git/pull/1003">now uses 64-bit tick counts</a> to avoid the (very rare) wraparound issue where it could miscalculate time differences every 49 days.</li>
<li>The <code>--no-lock-index</code> option of <code>git status</code> <a href="https://github.com/git-for-windows/git/pull/1004">is now also respected also in submodules</a>.</li>
<li>The regression of v2.11.0 where Git could no longer push to shared folders via UNC paths <a href="https://github.com/git-for-windows/git/issues/979">is fixed</a>.</li>
<li>A bug in the MSYS2 runtime where it performed POSIX->Windows argument conversion incorrectly <a href="https://github.com/git-for-windows/msys2-runtime/commit/3cf1b9c3ac4c5490bc94b00cc44682d2637d0b95">was fixed</a>.</li>
<li>The MSYS2 runtime <a href="https://github.com/git-for-windows/msys2-runtime/commit/5fe6d81012e97a348608511450f6a63750c906b6">was prepared to access the <code>FAST_CWD</code> internal data structure in upcoming Windows versions</a>.</li>
<li><a href="https://github.com/git-for-windows/git/commit/ecb88230d10382833dc961f83cd1092b8d0a2af2">Fixed a bug</a> in the experimental builtin difftool where it would not handle copied/renamed files properly.</li>
</ul>

</div><h2 id="v2.11.0" nr="106" class="collapsible"> Changes in v2.11.0<br /><small>since  v2.10.2 (November 2nd 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.11.0/Documentation/RelNotes/2.11.0.txt">Git v2.11.0</a>.</li>
<li>Performance of <code>git add</code> in large worktrees <a href="https://github.com/git-for-windows/git/pull/971">was improved</a>.</li>
<li>A <a href="https://github.com/git-for-windows/git/commit/5f3656e4b4b8ceeff40bc7fcf03aba3560bff17c">new, experimental, builtin version of the difftool</a> is available as <a href="https://github.com/git-for-windows/build-extra/commit/74339bdd9fab9fbf890f079c9024ff4f1309bb6d">an opt-in feature</a>.</li>
<li>Support <a href="https://github.com/git-for-windows/git/commit/056b41311688e9f433fe28e6b3aa6687fa36ca70">has been added</a> to generate project files for Visual Studio 2010 and later.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The preload-index feature <a href="https://github.com/git-for-windows/git/pull/955">now behaves much better in conjunction with sparse checkouts</a>.</li>
<li>When encountering a symbolic link, Git <a href="https://github.com/git-for-windows/git/issues/958">now always tries to read it</a>, not only when <code>core.symlinks = true</code>.</li>
<li>The regression where Git would not interpret non-ASCII characters passed from a CMD window correctly <a href="https://github.com/git-for-windows/git/issues/945">has been fixed</a>.</li>
<li>Performance of the cache of case-insensitive file names <a href="https://github.com/git-for-windows/git/pull/964">has been improved</a>.</li>
<li>When building with MS Visual C, <a href="https://github.com/git-for-windows/git/pull/948">release builds are now properly optimized</a>.</li>
<li><code>git cvsexportcommit</code> <a href="https://github.com/git-for-windows/git/pull/938">now also works with CVSNT</a>.</li>
<li>Git's Perl <a href="https://github.com/git-for-windows/git/issues/963">no longer gets confused by externally-set <code>PERL5LIB</code></a>.</li>
<li>The uninstaller <a href="https://github.com/git-for-windows/git/issues/909">no longer leaves an empty <code>Git\mingw64</code> folder behind</a>.</li>
<li>The installer <a href="https://github.com/git-for-windows/build-extra/commit/6da8414b8c75c76fa526bd75fec22eaefad88e09">now actually records</a> whether the user chose to enable or disable the Git Credential Manager.</li>
<li>A certain scenario that could cause a crash in cherry-pick <a href="https://github.com/git-for-windows/git/issues/952">no longer causes that</a>.</li>
</ul>

</div><h2 id="v2.10.2" nr="107" class="collapsible"> Changes in v2.10.2<br /><small>since  v2.10.1(2) (October 13th 2016)</h2></small><div>

<p>Git for windows v2.10.1(2) was a MinGit-only release (i.e. there was no Git for windows installer for that version).</p>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.10.2/Documentation/RelNotes/2.10.2.txt">Git v2.10.2</a>.</li>
<li>Comes with Git Credential Manager <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.8.1">v1.8.1</a>.</li>
<li>Comes with cURL <a href="https://github.com/curl/curl/releases/tag/curl-7_51_0">v7.51.0</a>.</li>
<li>Git for Windows <a href="https://github.com/git-for-windows/git/pull/773">can now be built easily with Visual C++ 2015</a>.</li>
<li>The installer <a href="https://github.com/git-for-windows/build-extra/commit/8332900af09116544f1bee8d20bbfd77daf3186f">now logs <code>post-install</code> errors more verbosely</a>.</li>
<li>A new option asks the installer <a href="https://github.com/git-for-windows/build-extra/commit/410b4b13505a8a25b199f5cbad0f4afa1a698f34">to skip installation if Git's files are in use</a>.</li>
<li>A new option asks the installer <a href="https://github.com/git-for-windows/build-extra/commit/c7bc72a157960ee9eef644141f116060c6c31c14">to quietly skip downgrading Git for Windows</a>, without indicating failure.</li>
<li>There is <a href="https://github.com/git-for-windows/git/issues/921">now an explicit option for symbolic link support</a>, including a link to a more verbose explanation of the issue.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>when upgrading Git for Windows, SSH agent processes <a href="https://github.com/git-for-windows/git/issues/920">are now auto-terminated</a>.</li>
<li>When trying to install/upgrade on a Windows version that is no longer supported, <a href="https://github.com/git-for-windows/git/issues/928">we now refuse to do so</a>.</li>
</ul>

</div><h2 id="v2.10.1(2)" nr="108" class="collapsible"> Changes in v2.10.1(2)<br /><small>since  v2.10.1 (October 4th 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>The speed of the SHA-1 calculation was improved by <a href="https://github.com/git-for-windows/git/pull/915">using OpenSSL's routines</a> which leverages features of current Intel hardware.</li>
<li>The <code>git reset</code> command <a href="https://github.com/git-for-windows/git/commit/6a6c0e84720ab5a374b61341ba9ab645ffafd35f">learned the (still experimental) <code>--stdin</code> option</a>.</li>
</ul>

</div><h2 id="v2.10.1" nr="109" class="collapsible"> Changes in v2.10.1<br /><small>since  v2.10.0 (September 3rd 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.10.1/Documentation/RelNotes/2.10.1.txt">Git v2.10.1</a>.</li>
<li>Comes with Git Credential Manager <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.7.0">v1.7.0</a>.</li>
<li>Comes with <a href="https://github.com/petervanderdoes/gitflow-avh/releases/tag/1.10.0">Git Flow v1.10.0</a>.</li>
<li>We <a href="https://github.com/git-for-windows/build-extra/pull/128">now produce nice diffs for <code>.docm</code> and <code>.dotm</code> files</a>, just as we did for <code>.docx</code> files already.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The icon in the Explorer integration ("Git Bash Here"), which was lost by mistake in v2.10.0, <a href="https://github.com/git-for-windows/git/issues/870">is back</a>.</li>
<li><a href="https://github.com/git-for-windows/git/commit/c4f481a41de66d24f6f9943104600f2e4f24b152">Fixed a crash</a> when calling <code>git diff -G&lt;regex&gt;</code> on new-born files without configured user diff drivers.</li>
<li>Interactive GPG signing of commits and tags <a href="https://github.com/git-for-windows/git/issues/871">was fixed</a>.</li>
<li>Calling Git with <code>--date=format:&lt;invalid-format&gt;</code> <a href="https://github.com/git-for-windows/git/issues/863">no longer results in an out-of-memory</a> but reports the problem and aborts instead.</li>
<li>Git Bash <a href="https://github.com/git-for-windows/git/issues/580">now opens properly even for Azure AD accounts</a>.</li>
<li>Git GUI <a href="https://github.com/git-for-windows/git/issues/850">respects the <code>commit.gpgsign</code> setting again</a>.</li>
<li>Upgrades the bundled OpenSSL to <a href="https://www.openssl.org/news/cl102.txt">v1.0.2j</a>.</li>
</ul>

</div><h2 id="v2.10.0" nr="110" class="collapsible"> Changes in v2.10.0<br /><small>since  v2.9.3(2) (August 25th 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.10.0/Documentation/RelNotes/2.10.0.txt">Git v2.10.0</a>.</li>
<li>The <code>git rebase -i</code> command was made faster <a href="https://github.com/git-for-windows/git/compare/3259f1f348b8173050c269dde7dc02346db759f3^...3259f1f348b8173050c269dde7dc02346db759f3^2">by reimplementing large parts in C</a>.</li>
<li>After helping the end-users to use the new defaults for PATH and FSCache, the installer <a href="https://github.com/git-for-windows/build-extra/compare/a0a8613c54c0bd651904432f07f7b2999790b097~2...a0a8613c54c0bd651904432f07f7b2999790b097">now respects the saved settings again</a>.</li>
<li><code>git version --build-options</code> now <a href="https://github.com/git-for-windows/git/pull/866">also reports the architecture</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>When upgrading Git for Windows, the installer <a href="https://github.com/git-for-windows/build-extra/commit/6682a86026e801d9c88c1903d5bd4dd1a0d79c4e">no longer opens a second window while uninstalling the previous version</a>.</li>
<li>Git for Windows' SDK <a href="https://github.com/git-for-windows/build-extra/commit/955e82b25a825f005946e7e4951e29404370aa94">can build an installer out of the box again</a>, without requiring an extra package to be installed.</li>
</ul>

</div><h2 id="v2.9.3(2)" nr="111" class="collapsible"> Changes in v2.9.3(2)<br /><small>since  v2.9.3 (August 13th 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git Credential Manager <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.6.1">v1.6.1</a>.</li>
<li>The feature introduced with Git for Windows v2.9.3 where <code>cat-file</code> can apply smudge filters <a href="https://github.com/git-for-windows/git/compare/f080fe716^...f080fe716">was renamed to <code>--filters</code> and made compatible with the <code>--batch</code> mode (the former option name <code>--smudge</code> has been deprecated and will go away in v2.10.0)</a>.</li>
<li>Comes with OpenSSH <a href="https://github.com/git-for-windows/MSYS2-packages/compare/da63f58~3...da63f58">7.3p1</a>.</li>
<li>Git's .exe files are now <a href="https://github.com/git-for-windows/build-extra/commit/3e9b83526">code-signed</a>, helping with performance when being run with <a href="https://en.wikipedia.org/wiki/Windows_File_Protection">Windows File Protection</a>.</li>
</ul>

</div><h2 id="v2.9.3" nr="112" class="collapsible"> Changes in v2.9.3<br /><small>since  v2.9.2 (July 16th 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.9.3/Documentation/RelNotes/2.9.3.txt">Git 2.9.3</a>.</li>
<li>Updated Git Credential Manager to <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v.1.6.0">version 1.6.0</a>.</li>
<li>Includes support for <code>git status --porcelain=v2</code>.</li>
<li>Avoids evaluating unnecessary patch IDs when determining which commits do not need to be rebased because they are already upstream.</li>
<li>Sports a new <code>--smudge</code> option for <code>git cat-file</code> that lets it pass blob contents through smudge filters configured for the specified path.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>When offering to <code>Launch Git Bash</code> after the installation, <a href="https://github.com/git-for-windows/build-extra/commit/aa0b462">it now launches in the home directory</a>, consistent with the <code>Git Bash</code> Start Menu entry.</li>
<li>When <code>~/.gitconfig</code> sets <code>core.hideDotFiles=false</code>, <code>git init</code> <a href="https://github.com/git-for-windows/git/issues/789">respects that again</a>.</li>
</ul>

</div><h2 id="v2.9.2" nr="113" class="collapsible"> Changes in v2.9.2<br /><small>since  v2.9.0 (June 14th 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.9.2/Documentation/RelNotes/2.9.2.txt">Git 2.9.2</a> (skipping the Windows release of <a href="https://github.com/git/git/blob/v2.9.1/Documentation/RelNotes/2.9.1.txt">Git 2.9.1</a> due to a regression caught by the automated tests).</li>
<li>Git Credential Manager was updated to <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.5.0">v1.5.0</a>.</li>
<li>The installer <a href="https://github.com/git-for-windows/build-extra/commit/82dc6284">will now refuse to downgrade Git for Windows, unless the user assures that it is intended</a>.</li>
<li>MinGit, the portable, non-interactive Git intended for third-party tools, <a href="https://github.com/git-for-windows/build-extra/commit/16a8cf5">is now also built as part of Git for Windows' official versions</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>When <code>git bundle create</code> is asked to create an empty bundle, it is supposed to error out and delete the corrupt bundle file. The deletion <a href="https://github.com/git-for-windows/git/pull/797">no longer fails due to an unreleased lock file</a>.</li>
<li>When launching <code>git help &lt;command&gt;</code>, the <code>help.browser</code> config setting <a href="https://github.com/git-for-windows/git/pull/793">is now respected</a>.</li>
<li>The title bar in Git for Windows' SDK <a href="https://github.com/git-for-windows/build-extra/pull/122">shows the correct prefix again</a>.</li>
<li>We <a href="https://github.com/git-for-windows/git/commit/ac008b30ec070f459450d602c55d55816aae2915">no longer throw an assertion</a> when using the <code>git credential-store</code>.</li>
<li>When configuring <code>notepad</code> as commit message editor, <a href="https://github.com/git-for-windows/build-extra/pull/123">UTF-8 messages are now handled correctly</a>.</li>
</ul>

</div><h2 id="v2.9.0" nr="114" class="collapsible"> Changes in v2.9.0<br /><small>since  v2.8.4 (June 7th 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.9.0/Documentation/RelNotes/2.9.0.txt">Git 2.9.0</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>When running <code>git gc --aggressive</code> or <code>git repack -ald</code> in the presence of multiple pack files, the command still had open handles to the pack files it wanted to remove. This <a href="https://github.com/git-for-windows/git/commit/85bc5ad9a69fa120b23471d483dc8da35d771ab7">has been fixed</a>.</li>
</ul>

</div><h2 id="v2.8.4" nr="115" class="collapsible"> Changes in v2.8.4<br /><small>since  v2.8.3 (May 20th 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.8.4/Documentation/RelNotes/2.8.4.txt">Git 2.8.4</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Child processes <a href="https://github.com/git-for-windows/git/pull/755">no longer inherit handles to temporary files</a>, which previously could prevent <code>index.lock</code> from being deleted.</li>
<li>When configuring Git Bash with Windows' default console, it <a href="https://github.com/git-for-windows/build-extra/pull/118">no longer loses its icon</a>.</li>
</ul>

</div><h2 id="v2.8.3" nr="116" class="collapsible"> Changes in v2.8.3<br /><small>since  v2.8.2 (May 3rd 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/blob/v2.8.3/Documentation/RelNotes/2.8.3.txt">Git v2.8.3</a>.</li>
</ul>

</div><h2 id="v2.8.2" nr="117" class="collapsible"> Changes in v2.8.2<br /><small>since  v2.8.1 (April 4th 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="https://github.com/git/git/raw/v2.8.2/Documentation/RelNotes/2.8.2.txt">Git v2.8.2</a>.</li>
<li>Starting with version 2.8.2, <a href="https://www.nuget.org/packages/GitForWindows/">Git for Windows is also published as a NuGet package</a>.</li>
<li>Comes with Git Credential Manager v1.3.0.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>FSCache <a href="https://github.com/git-for-windows/build-extra/commit/a1ae146">is now enabled by default</a> even when upgrading from previous Git for Windows versions.</li>
<li>We now add <code>git.exe</code> to the <code>PATH</code> <a href="https://github.com/git-for-windows/build-extra/commit/1e2e00e">by default</a> even when upgrading from previous Git for Windows versions.</li>
<li>Git GUI <a href="https://github.com/git-for-windows/git/pull/726">now sets author information correctly when amending</a>.</li>
<li>OpenSSL received a critical update to <a href="https://www.openssl.org/news/newslog.html">version 1.0.2h</a>.</li>
</ul>

</div><h2 id="v2.8.1" nr="118" class="collapsible"> Changes in v2.8.1<br /><small>since  v2.8.0 (March 29th 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="http://article.gmane.org/gmane.linux.kernel/2189878">Git v2.8.1</a>.</li>
<li>The Git for Windows project updated its contributor guidelines to the <a href="https://github.com/git-for-windows/git/pull/661">Contributor Covenant 1.4</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git's default editor (<code>vim</code>) is <a href="https://github.com/git-for-windows/msys2-runtime/commit/1ca92fa2ef89bf9d61d3911a499d8187db18427a">no longer freezing</a> in CMD windows.</li>
<li>GIT_SSH (and other executable paths that Git wants to spawn) <a href="https://github.com/git-for-windows/git/issues/692">can now contain spaces</a>.</li>
</ul>

</div><h2 id="v2.8.0" nr="119" class="collapsible"> Changes in v2.8.0<br /><small>since  v2.7.4 (March 18th 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="http://article.gmane.org/gmane.linux.kernel/2185094">Git v2.8.0</a>.</li>
<li>Comes with the <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.2.2">Git Credential Manager v1.2.2</a>.</li>
<li>The FSCache feature (which was labeled experimental for quite some time) <a href="https://github.com/git-for-windows/build-extra/pull/101">is now enabled by default</a>.</li>
<li>Git is now <a href="https://github.com/git-for-windows/build-extra/pull/102">added to the <code>PATH</code> by default</a> (previously, the default was for Git to be available only from Git Bash/CMD).</li>
<li>The installer <a href="https://github.com/git-for-windows/build-extra/pull/103">now offers to launch the Git Bash right away</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The previous workaround for the blurred link to the Git Credential Manager <a href="https://github.com/git-for-windows/build-extra/commit/58d978cb84096bcc887170cbfcf44af022848ae3">was fixed</a> so that the link is neither blurry nor overlapping.</li>
<li>The installer <a href="https://github.com/git-for-windows/build-extra/pull/104">now changes the label of the <code>Next</code> button to <code>Install</code></a> on the last wizard page before installing.</li>
</ul>

</div><h2 id="v2.7.4" nr="120" class="collapsible"> Changes in v2.7.4<br /><small>since  v2.7.3 (March 15th 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="http://article.gmane.org/gmane.linux.kernel/2179363">Git 2.7.4</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The Git Credential Manager hyperlink in the installer <a href="https://github.com/git-for-windows/build-extra/commit/28bb2a330323ba1c69f278cafa81e3e4fd3bf71c">is no longer blurred</a>.</li>
</ul>

</div><h2 id="v2.7.3" nr="121" class="collapsible"> Changes in v2.7.3<br /><small>since  v2.7.2 (February 23rd 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Git for Windows <a href="https://github.com/git-for-windows/git/issues/466">now ships with</a> the <a href="https://github.com/Microsoft/Git-Credential-Manager-for-Windows/">Git Credential Manager for Windows</a>.</li>
<li>Comes with <a href="http://article.gmane.org/gmane.linux.kernel/2174435">Git v2.7.3</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>We <a href="https://github.com/git-for-windows/git/issues/665">now handle UTF-8 merge and squash messages correctly in Git GUI</a>.</li>
<li>When trying to modify a repository config outside of any Git worktree, <a href="https://github.com/git-for-windows/git/commit/64acc338c"><code>git config</code> no longer creates a <code>.git/</code> directory</a> but prints an appropriate error message instead.</li>
<li>A new version of Git for Windows' SDK <a href="https://github.com/git-for-windows/build-extra/releases/git-sdk-1.0.3] that [works around pacman-key issues](https://github.com/git-for-windows/git/issues/670">was released</a>.</li>
<li>We <a href="https://github.com/git-for-windows/git/pull/677">no longer show asterisks when reading the username for credentials</a>.</li>
</ul>

</div><h2 id="v2.7.2" nr="122" class="collapsible"> Changes in v2.7.2<br /><small>since  v2.7.1(2) (February 12th 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Git for Windows' SDK version 1.0.2 <a href="https://github.com/git-for-windows/build-extra/releases/tag/git-sdk-1.0.2">has been released</a>.</li>
<li>The "list references" window of <code>gitk</code> <a href="https://github.com/git-for-windows/git/pull/620">is now wider by default</a>.</li>
<li>Comes with <a href="http://article.gmane.org/gmane.linux.kernel/2158401">Git 2.7.2</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The user is <a href="https://github.com/git-for-windows/git/issues/527">now presented with a nice error message</a> when calling <code>node</code> while <code>node.exe</code> is not in the <code>PATH</code> (this bug also affected other interactive console programs such as <code>python</code> and <code>php</code>).</li>
<li>The arrow keys <a href="https://github.com/git-for-windows/git/issues/495">are respected again in gitk</a>.</li>
<li>When a too-long path is encountered, <code>git clean -dfx</code> <a href="https://github.com/git-for-windows/git/issues/521">no longer aborts quietly</a>.</li>
<li>Git GUI learned to <a href="https://github.com/git-for-windows/git/issues/515">stage lines appended to a single-line file</a>.</li>
<li>When launching <code>C:\Program Files\Git\bin\bash -l -i</code> in a cmd window and pressing Ctrl+C, <a href="https://github.com/git-for-windows/git/pull/205">the console is no longer corrupted</a> (previously, the <code>bash.exe</code> redirector would terminate and both cmd &amp; Bash would compete for user input).</li>
</ul>

</div><h2 id="v2.7.1(2)" nr="123" class="collapsible"> Changes in v2.7.1(2)<br /><small>since  v2.7.1 (February 6th 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>The context menu items in the explorer <a href="https://github.com/git-for-windows/build-extra/pull/97">now show icons</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>A bug <a href="https://github.com/git-for-windows/git/commit/4abc31070f683e555de95331da0990052f55caa5">was fixed</a> where worktrees would forget their location e.g. after an interactive rebase.</li>
<li>Thanks to Eric Lawrence and Martijn Laan, <a href="https://github.com/git-for-windows/build-extra/tree/HEAD/installer/InnoSetup">our installer sports a better way to look for system files now</a>.</li>
</ul>

</div><h2 id="v2.7.1" nr="124" class="collapsible"> Changes in v2.7.1<br /><small>since  v2.7.0(2) (February 2nd 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="http://article.gmane.org/gmane.comp.version-control.git/285657">Git 2.7.1</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git GUI now <a href="https://github.com/git-for-windows/git/issues/410">starts properly even when the working directory contains non-ASCII characters</a>.</li>
<li>We forgot to enable Address Space Layout Randomization and Data Execution Prevention on our Git wrapper, and this is <a href="//github.com/git-for-windows/git/issues/644">now fixed</a>.</li>
<li>A bug in one of the DLLs used by Git for Windows <a href="https://github.com/Alexpux/MINGW-packages/pull/1051">was fixed</a> that prevented Git from working properly in 64-bit setups where <a href="https://technet.microsoft.com/en-us/library/cc779664%28v=ws.10%29.aspx">the <code>FLG_LDR_TOP_DOWN</code> global flag</a> is set.</li>
</ul>

</div><h2 id="v2.7.0(2)" nr="125" class="collapsible"> Changes in v2.7.0(2)<br /><small>since  v2.7.0 (January 5th 2016)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>To stave off exploits, Git for Windows <a href="https://github.com/git-for-windows/git/pull/612">now uses Address Space Layout Randomization (ASLR) and Data Execution Prevention (DEP)</a>.</li>
<li>Git for Windows' support for <code>git pull --rebase=interactive</code> that was dropped when the <code>pull</code> command was rewritten in C, <a href="https://github.com/git/git/commit/f9219c0b3">was resurrected</a>.</li>
<li>The installers are now <a href="https://github.com/git-for-windows/git/issues/592">dual signed</a> with SHA-2 and SHA-1 certificates.</li>
<li>The uninstaller <a href="https://github.com/git-for-windows/git/issues/540">is signed now, too</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>When installing as administrator, we <a href="https://github.com/git-for-windows/build-extra/commit/a13ffd7c3fa24e2ac1ef3561d7a7f09a0b924338">no longer offer the option to install quiicklaunch icons</a> because quicklaunch icons can only be installed per-user.</li>
<li>If a <code>~/.bashrc</code> is detected without a <code>~/.bash_profile</code>, the generated file will now <a href="https://github.com/git-for-windows/build-extra/pull/91">also source <code>~/.profile</code> if that exists</a>.</li>
<li>The environment variable <code>HOME</code> can now be used to set the home directory <a href="https://github.com/git-for-windows/msys2-runtime/commit/9660c5ffe82b921dd2193efa18e9721f47a6b22f">even when running with accounts that are part of a different domain than the current (non-domain-joined) machine</a> (in which case the MSYS2 runtime has no way to emulate POSIX-style UIDs).</li>
<li>Git <a href="https://github.com/Alexpux/MINGW-packages/pull/986">can now fetch and push via HTTPS</a> even when the <code>http.sslCAInfo</code> config variable was unset.</li>
<li>Git for Windows is now <a href="https://github.com/git-for-windows/git/pull/606">handling the case gracefully where the current user has no permission to list the parent of the current directory</a>.</li>
<li>More file locking issues ("Unlink of file ... failed. Should I try again?") <a href="https://github.com/git-for-windows/git/issues/500">were fixed</a>.</li>
</ul>

</div><h2 id="v2.7.0" nr="126" class="collapsible"> Changes in v2.7.0<br /><small>since  v2.6.4 (December 14th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="http://article.gmane.org/gmane.linux.kernel/2118402">Git v2.7.0</a>.</li>
</ul>

<h2>Bug Fixes</h2>

<ul>
<li>Non-ASCII command-lines are now <a href="https://github.com/git-for-windows/msys2-runtime/commit/4c362726c41102173613658">passed properly</a> to shell scripts.</li>
</ul>

</div><h2 id="v2.6.4" nr="127" class="collapsible"> Changes in v2.6.4<br /><small>since  v2.6.3 (November 10th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="http://article.gmane.org/gmane.linux.kernel/2103498">Git v2.6.4</a>.</li>
<li>Also available as <code>.tar.bz2</code> packages (you need an MSYS2/Cygwin-compatible unpacker to recreate the symbolic links correctly).</li>
</ul>

<h2>Bug Fixes</h2>

<ul>
<li>Git for Windows v2.6.3's installer <a href="https://github.com/git-for-windows/git/issues/523">failed</a> to <a href="https://github.com/git-for-windows/git/issues/526">elevate privileges automatically</a> (reported <a href="https://github.com/git-for-windows/git/issues/528">three times</a>, making it a charm), and as a consequence Git for Windows 2.6.3 was frequently <a href="https://github.com/git-for-windows/build-extra/commit/23672af723da18e5bc3c679e52106de3c2dec55a">installed per-user by mistake</a></li>
<li>The bug where <a href="https://github.com/git-for-windows/git/issues/542"><code>SHELL_PATH</code> had spaces</a> and that was <a href="https://github.com/git-for-windows/git/issues/498">reported</a> multiple <a href="https://github.com/git-for-windows/git/issues/468">times</a> has been <a href="https://github.com/git-for-windows/msys2-runtime/commit/7f4284d245f9c736dc8ec52e12c5d67cea7e4ba9">fixed</a>.</li>
<li>An additional work-around from upstream Git for <code>SHELL_PATH</code> containing spaces (fixing <a href="https://github.com/git-for-windows/git/issues/542">problems with interactive rebase's <code>exec</code> command</a> has been applied.</li>
</ul>

</div><h2 id="v2.6.3" nr="128" class="collapsible"> Changes in v2.6.3<br /><small>since  v2.6.2 (October 19th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with <a href="http://article.gmane.org/gmane.comp.version-control.git/280947">Git v2.6.3</a>.</li>
<li><a href="https://github.com/git-for-windows/git/issues/501">Enables the stack smasher to protect against buffer overflows</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git Bash <a href="https://github.com/git-for-windows/git/issues/509">works now even when choosing Windows' default console <em>and</em> installing into a short path (e.g. <code>C:\Git</code>)</a>.</li>
<li>Notepad <a href="https://github.com/git-for-windows/git/issues/517">can now really be used to edit commit messages</a>.</li>
<li>Git's garbage collector <a href="https://github.com/git-for-windows/git/issues/423">now handles stale <code>refs/remotes/origin/HEAD</code> gracefully</a>.</li>
<li>The regression in Git for Windows 2.6.2 that it required administrator privileges to be installed <a href="https://github.com/git-for-windows/build-extra/pull/86">is now fixed</a>.</li>
<li>When <code>notepad</code> is configured as default editor, we no longer do anything specially <a href="https://github.com/git-for-windows/git/issues/488">unless editing files inside <code>.git/</code></a>.</li>
</ul>

</div><h2 id="v2.6.2" nr="129" class="collapsible"> Changes in v2.6.2<br /><small>since  v2.6.1 (October 5th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git v2.6.2</li>
<li>Users who are part of a Windows domain <a href="https://github.com/git-for-windows/git/pull/487">now have sensible default values</a> for <code>user.name</code> and <code>user.email</code>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>We <a href="https://github.com/git-for-windows/git/pull/486">no longer run out of page file space</a> when <code>git fetch</code>ing large repositories.</li>
<li>The description of Windows' default console is accurate now (the console became more powerful in Windows 10).</li>
<li><em>Git GUI</em> now respects the <a href="https://github.com/git-for-windows/git/issues/490">terminal emulation chosen at install time</a> when <a href="https://github.com/git-for-windows/git/pull/492">running the <em>Git Bash</em></a>.</li>
</ul>

</div><h2 id="v2.6.1" nr="130" class="collapsible"> Changes in v2.6.1<br /><small>since 2.6.0 (September 29th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.6.1</li>
<li>The installer <a href="https://github.com/git-for-windows/git/issues/454">now writes the file <code>/etc/install-options.txt</code></a> to record which options were chosen at install time.</li>
<li>Replaces <code>git flow</code> with <a href="https://github.com/petervanderdoes/gitflow-avh">the <em>AVH edition</em></a> which is maintained actively, in surprising and disappointing contrast to Vincent Driessen's very own project.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The <code>PATH</code> variable <a href="https://github.com/git-for-windows/git/issues/438">is now really left alone</a> when choosing the <em>"Use Git from Git Bash only"</em> option in the installer. Note that upgrading Git for Windows will call the previous version's uninstaller, which might still have that bug.</li>
<li>Git GUI's <em>Registry>Create Desktop Icon</em> <a href="https://github.com/git-for-windows/git/issues/448">now generates correct shortcuts</a>.</li>
<li>The <code>antiword</code> utility to render Word documents for use in <code>git diff</code> <a href="https://github.com/git-for-windows/git/issues/453">now works correctly</a>.</li>
<li>In 64-bit installations, we <a href="https://github.com/git-for-windows/git/issues/288">no longer set a pack size limit by default</a>.</li>
<li>When installing Git for Windows as regular user, <a href="https://github.com/git-for-windows/git/issues/455">the installer no longer tries to create privileged registry keys</a>.</li>
</ul>

</div><h2 id="v2.6.0" nr="131" class="collapsible"> Changes in v2.6.0<br /><small>since 2.5.3 (September 18th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.6.0</li>
<li>The <code>WhoUses.exe</code> tool to determine which process holds a lock on a given file (which was shipped with Git for Windows 1.x) <a href="https://github.com/git-for-windows/git/issues/408">gets installed alongside Git for Windows again</a>.</li>
<li>The values <code>CurrentVersion</code>, <code>InstallPath</code> and <code>LibexecPath</code> are <a href="https://github.com/git-for-windows/git/issues/427">added to the <code>HKEY_LOCAL_MACHINE\Software\GitForWindows</code> registry key</a> to help third-party add-ons to find us.</li>
<li>When fetching or pushing with Git <em>without</em> a console, we now <a href="https://github.com/git-for-windows/git/issues/428">fall back to Git GUI's <code>askpass</code> helper</a> to ask for pass phrases.</li>
<li>When run through <code>&lt;INSTALL_PATH&gt;\cmd\git.exe</code>, Git <a href="https://github.com/git-for-windows/git/issues/429">will find tools in <code>$HOME/bin</code></a> now.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The portable version avoids DLL search path problems <a href="https://github.com/git-for-windows/git/issues/390">even when installed into a FAT filesystem</a>.</li>
<li>Configuring <code>notepad</code> as editor without configuring a width for commit messages <a href="https://github.com/git-for-windows/git/issues/430">no longer triggers an error message</a>.</li>
<li>When using Windows' default console for <em>Git Bash</em>, <a href="https://github.com/git-for-windows/git/issues/396">the <code>.sh</code> file associations work again</a>.</li>
<li>Portable Git's <code>README</code> <a href="https://github.com/git-for-windows/build-extra/pull/83">is now clearer about the need to run <code>post-install.bat</code> when unpacking manually</a>.</li>
<li><a href="https://github.com/git-for-windows/git/issues/436">We use the <code>winpty</code> trick now</a> to run <code>ipython</code> interactively, too.</li>
<li>When the environment variable <code>HOME</code> is not set, we <a href="https://github.com/git-for-windows/git/issues/414">now</a> fall back <a href="https://github.com/git-for-windows/git/issues/434">correctly</a> to use <code>HOMEDRIVE</code> and <code>HOMEPATH</code>.</li>
<li>The home directory is now <a href="https://github.com/git-for-windows/git/issues/435">set correctly</a> when running as the <code>SYSTEM</code> user.</li>
<li>The environment variable <code>GIT_WORK_TREE</code> <a href="https://github.com/git-for-windows/git/issues/402">may now differ in lower/upper case with the Git's idea of the current working directory</a>.</li>
<li>Running <code>git clone --dissociate ...</code> <a href="https://github.com/git-for-windows/git/issues/446">no longer locks the pack files during the repacking phase</a>.</li>
<li>Upstream cURL fixes for NTLM proxy issues ("Unknown SSL error") <a href="https://github.com/git-for-windows/git/issues/373">were backported</a>.</li>
<li>The 64-bit version <a href="https://github.com/git-for-windows/git/issues/449">now includes</a> the <code>astextplain</code> script it lacked by mistake.</li>
</ul>

</div><h2 id="v2.5.3" nr="132" class="collapsible"> Changes in v2.5.3<br /><small>since 2.5.2(2) (September 13th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.5.3.</li>
<li>Includes <a href="http://nvie.com/posts/a-successful-git-branching-model/"><code>git flow</code></a>.</li>
<li>By configuring <code>git config core.editor notepad</code>, users <a href="https://github.com/git-for-windows/git/issues/381">can now use <code>notepad.exe</code> as their default editor</a>. Configuring <code>git config format.commitMessageColumns 72</code> will be picked up by the notepad wrapper and line-wrap the commit message after the user edited it.</li>
<li>The Subversion bindings for use with <code>git svn</code> <a href="https://github.com/git-for-windows/git/issues/374">were upgraded to version 1.9.1</a>.</li>
<li>Some interactive console programs, e.g. <code>psql.exe</code>, <a href="https://github.com/git-for-windows/git/issues/399">now work in mintty thanks to pre-configured aliases</a>.</li>
<li>The mechanism to diff <code>.pdf</code>, <code>.doc</code> and <code>.docx</code> files known from Git for Windows 1.x <a href="https://github.com/git-for-windows/git/issues/355">has been ported to Git for Windows 2.x</a>.</li>
<li>Git can now <a href="https://github.com/git-for-windows/git/issues/370">access IPv6-only hosts via HTTP/HTTPS</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The <code>.vimrc</code> in the home directory <a href="https://github.com/git-for-windows/git/issues/364">is now allowed to have DOS line endings</a>.</li>
<li>The <code>README.portable</code> file of the portable Git <a href="https://github.com/git-for-windows/git/issues/394">mentions the need to run <code>post-install.bat</code></a> when the archive was extracted manually.</li>
<li>Home directories for user names <a href="https://github.com/git-for-windows/git/issues/331">with non-ASCII characters</a> are <a href="https://github.com/git-for-windows/git/issues/336">handled</a> correctly <a href="https://github.com/git-for-windows/git/issues/383">now</a>.</li>
<li>The documentation <a href="https://github.com/git-for-windows/git/issues/404">no longer shows plain-text <code>linkgit:...</code> "links"</a> but proper hyperlinks instead.</li>
<li>The <code>mtab</code> link <a href="https://github.com/git-for-windows/git/issues/405">is written to <code>/etc/mtab</code> again, as it should</a>.</li>
<li>When run inside the PowerShell, Git no longer gets confused when the current directory's path and what is recorded in the file system differs in case (e.g. "GIT/" vs "Git/").</li>
</ul>

</div><h2 id="v2.5.2(2)" nr="133" class="collapsible"> Changes in v2.5.2(2)<br /><small>since 2.5.2 (September 10th 2015)</h2></small><div>

<h3>Bug Fixes</h3>

<ul>
<li>The Git GUI <a href="https://github.com/git-for-windows/git/issues/376">can be launched from the Start menu again</a>.</li>
<li>It <a href="https://github.com/git-for-windows/git/pull/305">now works</a> to call <code>git add -p -- .</code> when there is a large number of files.</li>
<li>The Arrow keys can be used in the Bash history again <a href="https://github.com/git-for-windows/git/issues/353">when run in the Windows console</a>.</li>
<li>Tab completion in the context of a large Active Directory <a href="https://github.com/git-for-windows/git/issues/377">is no longer slow</a>.</li>
</ul>

</div><h2 id="v2.5.2" nr="134" class="collapsible"> Changes in v2.5.2<br /><small>since 2.5.1 (August 31th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.5.2</li>
<li>Alternates <a href="https://github.com/git-for-windows/git/pull/286">can now point to UNC paths</a>, i.e. network drives.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The MSYS2 runtime was taught <a href="https://github.com/git-for-windows/git/issues/193">not to look hard for groups</a>, speeding up <em>Git Bash</em>'s startup time.</li>
<li>A <a href="https://github.com/git-for-windows/git/issues/361">work around</a> was added for <a href="https://github.com/git-for-windows/git/wiki/32-bit-issues">issues</a> when installing 32-bit Git for Windows on 64-bit Windows 10.</li>
<li>The installer <a href="https://github.com/git-for-windows/git/issues/351">no longer freezes</a> when there are interactive commands in the user's <code>.profile</code>.</li>
<li><code>git rebase --skip</code> <a href="https://github.com/git-for-windows/git/issues/365">was speeded up again</a>.</li>
<li>The redirector in <code>/bin/bash.exe</code> now adjusts the <code>PATH</code> environment variable correctly (i.e. so that Git's executables are found) before launching the <em>real</em> Bash, even when called without <code>--login</code>.</li>
<li>When installing Git for Windows to a location whose path is longer than usual, Git commands <a href="https://github.com/git-for-windows/git/issues/303">no longer trigger occasional <code>Bad address</code> errors</a>.</li>
<li>Git <a href="https://github.com/git-for-windows/git/issues/329">no longer asks for a DVD to be inserted again</a> when one has been ejected from the <code>D:</code> drive.</li>
</ul>

</div><h2 id="v2.5.1" nr="135" class="collapsible"> Changes in v2.5.1<br /><small>since 2.5.0 (August 18th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.5.1</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Backspace <a href="https://github.com/git-for-windows/git/issues/282">works now</a> with ConHost-based (<code>cmd.exe</code>) terminal.</li>
<li>When there is a <code>~/.bashrc</code> but no <code>~/.bash_profile</code>, <a href="https://github.com/git-for-windows/build-extra/pull/71">the latter will be created automatically</a>.</li>
<li>When calling a non-login shell, <a href="https://github.com/git-for-windows/build-extra/pull/72">the prompt now works</a>.</li>
<li>The text in the installer describing the terminal emulator options <a href="https://github.com/git-for-windows/build-extra/pull/69">is no longer cut off</a>.</li>
<li>The <code>connect.exe</code> tool to allow SSH connections via HTTP/HTTPS/SOCKS proxies <a href="https://github.com/git-for-windows/build-extra/pull/73">is included in Git for Windows again</a>, as it was in Git for Windows 1.x.</li>
<li>The <code>LANG</code> variable is <a href="https://github.com/git-for-windows/git/issues/298">no longer left unset</a> (which caused troubles with vim).</li>
<li><code>call start-ssh-agent</code> <a href="https://github.com/git-for-windows/git/issues/314">no longer spits out bogus lines</a>.</li>
<li>It is now possible <a href="https://github.com/git-for-windows/git/issues/309">even behind NTLM-authenticated proxies</a> to install <a href="https://git-for-windows.github.io/#download-sdk">Git for Windows' SDK</a>.</li>
<li>We <a href="https://github.com/git-for-windows/git/issues/318">can handle the situation now</a> when the first <code>$PATH</code> elements point outside of Git for Windows' <code>bin/</code> directories and contain <code>.dll</code> files that interfere with our own (e.g. PostgreSQL's <code>libintl-8.dll</code>).</li>
<li>The <code>patch</code> tool <a href="https://github.com/git-for-windows/build-extra/pull/74">is now included again</a> as it was in Git for Windows 1.x.</li>
</ul>

</div><h2 id="v2.5.0" nr="136" class="collapsible"> Changes in v2.5.0<br /><small>since 2.4.6 (July 18th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.5.0</li>
<li>On Windows 7 and later, <a href="https://github.com/git-for-windows/git/issues/263">the <em>Git Bash</em> can now correctly be pinned to the task bar</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>The size of the installers <a href="https://github.com/git-for-windows/git/issues/262">was reduced again</a>, almost to the levels of Git for Windows 1.x.</li>
<li>Under certain circumstances, when the Windows machine is part of a Windows domain with lots of users, the startup of the <em>Git Bash</em> <a href="https://github.com/git-for-windows/git/issues/193">is now faster</a>.</li>
<li>Git <a href="https://github.com/git-for-windows/git/issues/255">no longer warns about being unable to read bogus Git attributes</a>.</li>
</ul>

</div><h2 id="v2.4.6" nr="137" class="collapsible"> Changes in v2.4.6<br /><small>since 2.4.5 (June 29th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.4.6</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git for Windows handles symlinks now, <a href="https://github.com/git-for-windows/git/pull/220">even if core.symlinks does not tell Git to generate symlinks itself</a>.</li>
<li><code>git svn</code> learned <a href="https://github.com/git-for-windows/git/pull/246"><em>not</em> to reuse incompatible on-disk caches left over from previous Git for Windows versions</a>.</li>
</ul>

</div><h2 id="v2.4.5" nr="138" class="collapsible"> Changes in v2.4.5<br /><small>since 2.4.4 (June 20th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.4.5</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Git Bash <a href="https://github.com/git-for-windows/git/issues/222">no longer crashes when called with <code>TERM=msys</code></a>. This reinstates compatibility with GitHub for Windows.</li>
</ul>

</div><h2 id="v2.4.4" nr="139" class="collapsible"> Changes in v2.4.4<br /><small>since 2.4.3 (June 12th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.4.4</li>
<li>The POSIX-to-Windows path mangling <a href="https://github.com/git-for-windows/msys2-runtime/pull/11">can now be turned off</a> by setting the <code>MSYS_NO_PATHCONV</code> environment variable. This even works for individual command lines: <code>MSYS_NO_PATHCONV=1 cmd /c dir /x</code> will list the files in the current directory along with their 8.3 versions.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li><code>git-bash.exe</code> <a href="https://github.com/git-for-windows/git/issues/130">no longer changes the working directory to the user's home directory</a>.</li>
<li>Git <a href="https://github.com/msysgit/git/issues/359">can now clone into a drive root</a>, e.g. <code>C:\</code>.</li>
<li>For backwards-compatibility, redirectors are installed into <code>/bin/bash.exe</code> and <code>/bin/git.exe</code>, e.g. <a href="https://github.com/git-for-windows/git/issues/208">to support SourceTree and TortoiseGit better</a>.</li>
<li>When using <code>core.symlinks = true</code> while cloning repositories with symbolic links pointing to directories, <a href="https://github.com/git-for-windows/git/issues/210"><code>git status</code> no longer shows bogus modifications</a>.</li>
</ul>

</div><h2 id="v2.4.3" nr="140" class="collapsible"> Changes in v2.4.3<br /><small>since 2.4.2 (May 27th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.4.3</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li><a href="https://github.com/git-for-windows/git/issues/163">We include <code>diff.exe</code></a> just as it was the case in Git for Windows 1.x</li>
<li>The certificates for accessing remote repositories via HTTPS <a href="https://github.com/git-for-windows/git/issues/168">are found on XP again</a>.</li>
<li><code>clear.exe</code> and the cursor keys in vi <a href="https://github.com/git-for-windows/git/issues/169">work again</a> when Git Bash is run in Windows' default console window ("ConHost").</li>
<li>The ACLs of the user's temporary directory are no longer modified when mounting <code>/tmp/</code> (https://github.com/git-for-windows/git/issues/190).</li>
<li><em>Git Bash Here</em> works even from the context menu of the empty area in Windows Explorer's view of C:\, D:\, etc (https://github.com/git-for-windows/git/issues/176).</li>
</ul>

</div><h2 id="v2.4.2" nr="141" class="collapsible"> Changes in v2.4.2<br /><small>since 2.4.1 (May 14th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>On Windows Vista and later, <a href="https://github.com/git-for-windows/git/pull/156">NTFS junctions can be used to emulate symlinks now</a>; To enable this emulation, the <code>MSYS</code> environment variable needs to be set to <code>winsymlinks:nativestrict</code>.</li>
<li>The <em>Git Bash</em> learned to support <a href="https://github.com/git-for-windows/git/commit/ac6b03cb4">several options to support running the Bash in arbitrary terminal emulators</a>.</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Just like Git for Windows 1.x, <a href="https://github.com/git-for-windows/build-extra/pull/59">pressing Shift+Tab in the Git Bash triggers tab completion</a>.</li>
<li><a href="https://github.com/git-for-windows/msys2-runtime/pull/9">Auto-mount the temporary directory of the current user to <code>/tmp/</code> again</a>, just like Git for Windows 1.x did (thanks to MSys1's hard-coded mount point).</li>
</ul>

</div><h2 id="v2.4.1" nr="142" class="collapsible"> Changes in v2.4.1<br /><small>since 2.4.0(2) (May 7th 2015)</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.4.1</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>When selecting the standard Windows console window for <code>Git Bash</code>, a regression was fixed that triggered <a href="https://github.com/git-for-windows/git/issues/148">an extra console window</a> to be opened.</li>
<li>The password <a href="https://github.com/git-for-windows/git/issues/124">can be entered interactively again</a> when <code>git push</code>ing to a HTTPS remote.</li>
</ul>

</div><h2 id="v2.4.0(2)" nr="143" class="collapsible"> Changes in v2.4.0(2)<br /><small>since 2.4.0 (May 5th 2015)</h2></small><div>

<h3>Bug Fixes</h3>

<ul>
<li>The <code>.sh</code> file association was fixed</li>
<li>The installer will now remove files from a previous Git for Windows versions, particularly important for 32-bit -> 64-bit upgrades</li>
</ul>

<h3>New Features</h3>

<ul>
<li>The installer now offers the choice between opening the <em>Git Bash</em> in a MinTTY (default) or a regular Windows console window (Git for Windows 1.x' setting).</li>
</ul>

</div><h2 id="v2.4.0" nr="144" class="collapsible"> Changes in v2.4.0<br /><small>since 2.3.7-preview20150429</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.4.0</li>
<li>Git for Windows now installs its configuration into a Windows-wide location: <code>%PROGRAMDATA%\Git\config</code> (which will be shared by libgit2-based applications with the next libgit2 version)</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Fixed a regression where <em>Git Bash</em> would not start properly on Windows XP</li>
<li>Tab completion works like on Linux and MacOSX (double-Tab required to show ambiguous completions)</li>
<li>In 32-bit setups, all the MSYS2 <code>.dll</code>'s address ranges are adjusted ("auto-rebased") as part of the installation process</li>
<li>The post-install scripts of MSYS2 are now executed as part of the installation process, too</li>
<li>All files that are part of the installation will now be registered so they are deleted upon uninstall</li>
</ul>

</div><h2 id="v2.3.7-preview20150429" nr="145" class="collapsible"> Changes in v2.3.7-preview20150429<br /><small>since 2.3.6-preview20150425</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.3.7</li>
</ul>

<h3>Bug Fix</h3>

<ul>
<li>A flawed "fix" that ignores submodules during rebases was dropped</li>
<li>The home directory can be overridden using the <code>$HOME</code> environment variable again</li>
</ul>

</div><h2 id="v2.3.6-preview20150425" nr="146" class="collapsible"> Changes in v2.3.6-preview20150425<br /><small>since 2.3.5-preview20150402</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.3.6</li>
</ul>

<h3>Bug Fixes</h3>

<ul>
<li>Fixed encoding issues in Git Bash and keept the TMP environment variable intact.</li>
<li>Downgraded the <code>nettle</code> packages due to an <a href="https://github.com/Alexpux/MINGW-packages/issues/549"><em>MSYS2</em> issue</a></li>
<li>A couple of fixes to the Windows-specific Git wrapper</li>
<li>Git wrapper now refuses to use <code>$HOMEDRIVE$HOMEPATH</code> if it points to a non-existing directory (this can happen if it points to a network drive that just so happens to be Disconnected Right Now).</li>
<li>Much smoother interaction with the <code>mintty</code> terminal emulator</li>
<li>Respects the newly introduced Windows-wide <code>%PROGRAMDATA%\Git\config</code> configuration</li>
</ul>

</div><h2 id="v2.3.5-preview20150402" nr="147" class="collapsible"> Changes in v2.3.5-preview20150402<br /><small>since 1.9.5-preview20150402</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 2.3.5 plus Windows-specific patches.</li>
<li>First release based on <a href="https://msys2.github.io/">MSYS2</a>.</li>
<li>Support for 64-bit!</li>
</ul>

<h3>Backwards-incompatible changes</h3>

<ul>
<li>The development environment changed completely from the previous version (maybe introducing some regressions).</li>
<li>No longer ships with Git Cheetah (because there are better-maintained Explorer extensions out there).</li>
</ul>

</div><h2 id="v1.9.5-preview20150402" nr="148" class="collapsible"> Changes in v1.9.5-preview20150402<br /><small>since 1.9.5-preview20141217</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.9.5 plus Windows-specific patches.</li>
<li>Make <code>vimdiff</code> usable with <code>git mergetool</code>.</li>
</ul>

<h3>Security Updates</h3>

<ul>
<li>Mingw-openssl to 0.9.8zf and msys-openssl to 1.0.1m</li>
<li>Bash to 3.1.23(6)</li>
<li>Curl to 7.41.0</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>ssh-agent: only ask for password if not already loaded</li>
<li>Reenable perl debugging ("perl -de 1" possible again)</li>
<li>Set icon background color for Windows 8 tiles</li>
<li>poll: honor the timeout on Win32</li>
<li>For <code>git.exe</code> alone, use the same HOME directory fallback mechanism as <code>/etc/profile</code></li>
</ul>

</div><h2 id="v1.9.5-preview20141217" nr="149" class="collapsible"> Changes in v1.9.5-preview20141217<br /><small>since 1.9.4-preview20140929</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.9.5 plus Windows-specific patches.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Safeguards against bogus file names on NTFS (CVE-2014-9390).</li>
</ul>

</div><h2 id="v1.9.4-preview20140929" nr="150" class="collapsible"> Changes in v1.9.4-preview20140929<br /><small>since 1.9.4-preview20140815</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.9.4 plus Windows-specific patches.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Update bash to patchlevel 3.1.20(4) (msysgit PR#254, msysgit issue #253).</li>
<li>Fixes CVE-2014-6271, CVE-2014-7169, CVE-2014-7186 and CVE-2014-7187.</li>
<li><code>gitk.cmd</code> now works when paths contain the ampersand (&amp;) symbol (msysgit PR #252)</li>
<li>Default to automatically close and restart applications in silent mode installation type</li>
<li><code>git svn</code> is now usable again (regression in previous update, msysgit PR#245)</li>
</ul>

</div><h2 id="v1.9.4-preview20140815" nr="151" class="collapsible"> Changes in v1.9.4-preview20140815<br /><small>since 1.9.4-preview20140611</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.9.4 plus Windows-specific patches</li>
<li>Add vimtutor (msysgit PR #220)</li>
<li>Update OpenSSH to 6.6.1p1 and its OpenSSL to 1.0.1i (msysgit PR #221, #223, #224, #226,  #229, #234, #236)</li>
<li>Update mingw OpenSSL to 0.9.8zb (msysgit PR #241, #242)</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Checkout problem with directories exceeding <code>MAX_PATH</code> (PR #212, msysgit #227)</li>
<li>Backport a webdav fix from <em>junio/maint</em> (d9037e http-push.c: make CURLOPT_IOCTLDATA a usable pointer, PR #230)</li>
</ul>

<h3>Regressions</h3>

<ul>
<li><code>git svn</code> is/might be broken. Fixes welcome.</li>
</ul>

</div><h2 id="v1.9.4-preview20140611" nr="152" class="collapsible"> Changes in v1.9.4-preview20140611<br /><small>since 1.9.2-preview20140411</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.9.4 plus Windows-specific patches.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Upgrade openssl to 0.9.8za (msysgit PR #212)</li>
<li>Config option to disable side-band-64k for transport (#101)</li>
<li>Make <code>git-http-backend</code>, <code>git-http-push</code>, <code>git-http-fetch</code> available again (#174)</li>
</ul>

</div><h2 id="v1.9.2-preview20140411" nr="153" class="collapsible"> Changes in v1.9.2-preview20140411<br /><small>since 1.9.0-preview20140217</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.9.2 plus Windows-specific patches.</li>
<li>Custom installer settings can be saved and loaded, for unsupervised installation on batches of machines (msysGit PR #168).</li>
<li>Comes with VIM 7.4 (msysGit PR #170).</li>
<li>Comes with ZLib 1.2.8.</li>
<li>Comes with xargs 4.4.2.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Work around stack limitations when listing an insane number of tags (PR #154).</li>
<li>Assorted test fixes (PRs #156, #158).</li>
<li>Compile warning fix in config.c (PR #159).</li>
<li>Ships with actual dos2unix and unix2dos.</li>
<li>The installer no longer recommends mixing with Cygwin.</li>
<li>Fixes a regression in Git-Cheetah which froze the Explorer upon calling Git Bash from the context menu (Git-Cheetah PRs #14 and #15).</li>
</ul>

</div><h2 id="v1.9.0-preview20140217" nr="154" class="collapsible"> Changes in v1.9.0-preview20140217<br /><small>since 1.8.5.2-preview20131230</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.9.0 plus Windows-specific patches.</li>
<li>Better work-arounds for Windows-specific path length limitations (pull request #122)</li>
<li>Uses optimized TortoiseGitPLink when detected (msysGit pull request #154)</li>
<li>Allow Windows users to use Linux Git on their files, using <a href="http://www.vagrantup.com/">Vagrant</a> (msysGit pull request #159)</li>
<li>InnoSetup 5.5.4 is now used to generate the installer (msysGit pull request #167)</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Fixed regression with interactive password prompt for remotes using the HTTPS protocol (issue #111)</li>
<li>We now work around Subversion servers printing non-ISO-8601-compliant time stamps (pull request #126)</li>
<li>The installer no longer sets the HOME environment variable (msysGit pull request #166)</li>
<li>Perl no longer creates empty <code>sys$command</code> files when no stdin is connected (msysGit pull request #152)</li>
</ul>

</div><h2 id="v1.8.5.2-preview20131230" nr="155" class="collapsible"> Changes in v1.8.5.2-preview20131230<br /><small>since 1.8.4-preview20130916</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.8.5.2 plus Windows-specific patches.</li>
<li>Windows-specific patches are now grouped into pseudo-branches which should make future development robust despite slow uptake of the Windows-specific patches by upstream git.git.</li>
<li>Works around more path length limitations (pull request #86)</li>
<li>Has an optional <code>stat()</code> cache toggled via <code>core.fscache</code> (pull request #107)</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Lots of installer fixes</li>
<li><code>git-cmd</code>: Handle home directory on a different drive correctly (pull request #146)</li>
<li><code>git-cmd</code>: add a helper to work with the ssh agent (pull request #135)</li>
<li>Git-Cheetah: prevent duplicate menu entries (pull request #7)</li>
<li>No longer replaces <code>dos2unix</code> with <code>hd2u</code> (a more powerful, but slightly incompatible version of dos2unix)</li>
</ul>

</div><h2 id="v1.8.4-preview20130916" nr="156" class="collapsible"> Changes in v1.8.4-preview20130916<br /><small>since 1.8.3-preview20130601</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.8.4 plus Windows specific patches.</li>
<li>Enabled unicode support in bash (#42 and #79)</li>
<li>Included <code>iconv.exe</code> to assist in writing encoding filters</li>
<li>Updated openssl to 0.9.8y</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Avoid emitting non-printing chars to set console title.</li>
<li>Various encoding fixes for the git test suite</li>
<li>Ensure wincred handles empty username/password.</li>
</ul>

</div><h2 id="v1.8.3-preview20130601" nr="157" class="collapsible"> Changes in v1.8.3-preview20130601<br /><small>since 1.8.1.2-preview20130201</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.8.3 plus Windows specific patches.</li>
<li>Updated curl to 7.30.0 with IPv6 support enabled.</li>
<li>Updated gnupg to 1.4.13</li>
<li>Installer improvements for update or reinstall options.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Avoid emitting color coded ls output to pipes.</li>
<li>ccache binary updated to work on XP.</li>
<li>Fixed association of .sh files setup by the installer.</li>
<li>Fixed registry-based explorer menu items for XP (#95)</li>
</ul>

</div><h2 id="v1.8.1.2-preview20130201" nr="158" class="collapsible"> Changes in v1.8.1.2-preview20130201<br /><small>since 1.8.0-preview20121022</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.8.1.2 plus Windows specific patches.</li>
<li>Includes support for using the Windows Credential API to store access credentials securely and provide access via the control panel tool to manage git credentials.</li>
<li>Rebase autosquash support is now enabled by default. See <a href="http://goo.gl/2kwKJ">http://goo.gl/2kwKJ</a> for some suggestions on using this.</li>
<li>All msysGit development is now done on 'master' and the devel branches are deleted.</li>
<li>Tcl/Tk upgraded to 8.5.13.</li>
<li>InnoSetup updated to 5.5.3 (Unicode)</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Some changes to avoid clashing with cygwin quite so often.</li>
<li>The installer will attempt to handle files mirrored in the virtualstore.</li>
</ul>

</div><h2 id="v1.8.0-preview20121022" nr="159" class="collapsible"> Changes in v1.8.0-preview20121022<br /><small>since 1.7.11-preview20120710</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.8.0 plus Windows specific patches.</li>
<li>InnoSetup updated to 5.5.2</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Fixed icon backgrounds on low color systems</li>
<li>Avoid installer warnings during writability testing.</li>
<li>Fix bash prompt handling due to upstream changes.</li>
</ul>

</div><h2 id="v1.7.11-preview20120710" nr="160" class="collapsible"> Changes in v1.7.11-preview20120710<br /><small>since 1.7.11-preview20120704</h2></small><div>

<h3>Bugfixes</h3>

<ul>
<li>Propagate error codes from git wrapper (issue #43, #45)</li>
<li>Include CAcert root certificates in SSL bundle (issue #37)</li>
</ul>

</div><h2 id="v1.7.11-preview20120704" nr="161" class="collapsible"> Changes in v1.7.11-preview20120704<br /><small>since 1.7.11-preview20120620</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with the beautiful Git logo from <a href="http://git-scm.com/downloads/logos">http://git-scm.com/downloads/logos</a></li>
<li>The installer no longer asks for the directory and program group when updating</li>
<li>The installer now also auto-detects TortoisePlink that comes with TortoiseGit</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Git::SVN is correctly installed again</li>
<li>The default format for git help is HTML again</li>
<li>Replaced the git.cmd script with an exe wrapper to fix issue #36</li>
<li>Fixed executable detection to speed up help -a display.</li>
</ul>

</div><h2 id="v1.7.11-preview20120620" nr="162" class="collapsible"> Changes in v1.7.11-preview20120620<br /><small>since 1.7.10-preview20120409</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.7.11 plus Windows specific patches.</li>
<li>Updated curl to 7.26.0</li>
<li>Updated zlib to 1.2.7</li>
<li>Updated Inno Setup to 5.5.0 and avoid creating symbolic links (issue #16)</li>
<li>Updated openssl to 0.9.8x and support reading certificate files from Unicode paths (issue #24)</li>
<li>Version resource built into <code>git</code> executables.</li>
<li>Support the Large Address Aware feature to reduce chance out-of-memory on 64 bit windows when repacking large repositories.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Please refer to the release notes for official Git 1.7.11.</li>
<li>Fix backspace/delete key handling in <code>rxvt</code> terminals.</li>
<li>Fixed TERM setting to avoid a warning from <code>less</code>.</li>
<li>Various fixes for handling unicode paths.</li>
</ul>

</div><h2 id="v1.7.10-preview20120409" nr="163" class="collapsible"> Changes in v1.7.10-preview20120409<br /><small>since 1.7.9-preview20120201</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.7.10 plus Windows specific patches.</li>
<li>UTF-8 file name support.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Please refer to the release notes for official Git 1.7.10.</li>
<li>Clarifications in the installer.</li>
<li>Console output is now even thread-safer.</li>
<li>Better support for foreign remotes (Mercurial remotes are disabled for now, due to lack of a Python version that can be compiled within the development environment).</li>
<li>Git Cheetah no longer writes big log files directly to <code>C:\</code>.</li>
<li>Development environment: enhancements in the script to make a 64-bit setup.</li>
<li>Development environment: enhancements to the 64-bit Cheetah build.</li>
</ul>

</div><h2 id="v1.7.9-preview20120201" nr="164" class="collapsible"> Changes in v1.7.9-preview20120201<br /><small>since 1.7.8-preview20111206</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.7.9 plus Windows specific patches.</li>
<li>Improvements to the installer running application detection.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Please refer to the release notes for official Git 1.7.9</li>
<li>Fixed initialization of the git-cheetah submodule in net-installer.</li>
<li>Fixed duplicated context menu items with git-cheetah on Windows 7.</li>
<li>Patched gitk to display filenames when run on a subdirectory.</li>
<li>Tabbed gitk preferences dialog to allow use on smaller screens.</li>
</ul>

</div><h2 id="v1.7.8-preview20111206" nr="165" class="collapsible"> Changes in v1.7.8-preview20111206<br /><small>since 1.7.7.1-preview20111027</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.7.8 plus Windows specific patches.</li>
<li>Updated Tcl/Tk to 8.5.11 and libiconv to 1.14</li>
<li>Some changes to support building with MSVC compiler.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Please refer to the release notes for official Git 1.7.8</li>
<li>Git documentation submodule location fixed.</li>
</ul>

</div><h2 id="v1.7.7.1-preview20111027" nr="166" class="collapsible"> Changes in v1.7.7.1-preview20111027<br /><small>since 1.7.7-preview20111014</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.7.7.1 plus patches.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Please refer to the release notes for official Git 1.7.7.1</li>
<li>Includes an important upstream fix for a bug that sometimes corrupts the git index file.</li>
</ul>

</div><h2 id="v1.7.7-preview20111014" nr="167" class="collapsible"> Changes in v1.7.7-preview20111014<br /><small>since 1.7.6-preview20110708</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.7.7 plus patches.</li>
<li>Updated gzip/gunzip and include <code>unzip</code> and <code>gvim</code></li>
<li>Primary repositories moved to <a href="http://github.com/msysgit/">GitHub</a></li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Please refer to the release notes for official Git 1.7.7</li>
<li>Re-enable <code>vim</code> highlighting</li>
<li>Fixed issue with <code>libiconv</code>/<code>libiconv-2</code> location</li>
<li>Fixed regressions in Git Bash script</li>
<li>Fixed installation of mergetools for <code>difftool</code> and <code>mergetool</code> use and launching of beyond compare on windows.</li>
<li>Fixed warning about mising hostname during <code>git fetch</code></li>
</ul>

</div><h2 id="v1.7.6-preview20110708" nr="168" class="collapsible"> Changes in v1.7.6-preview20110708<br /><small>since 1.7.4-preview20110211</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.7.6 plus patches.</li>
<li>Updates to various supporting tools (openssl, iconv, InnoSetup)</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Please refer to the release notes for official Git 1.7.6</li>
<li>Fixes to msys compat layer for directory entry handling and command line globbing.</li>
</ul>

</div><h2 id="v1.7.4-preview20110211" nr="169" class="collapsible"> Changes in v1.7.4-preview20110211<br /><small>since 1.7.3.2-preview20101025</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.7.4 plus patches.</li>
<li>Includes antiword to enable viewing diffs of <code>.doc</code> files</li>
<li>Includes poppler to enable viewing diffs of <code>.pdf</code> files</li>
<li>Removes cygwin paths from the bash shell PATH</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Please refer to the release notes for official Git 1.7.4</li>
</ul>

</div><h2 id="v1.7.3.2-preview20101025" nr="170" class="collapsible"> Changes in v1.7.3.2-preview20101025<br /><small>since 1.7.3.1-preview20101002</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.7.3.2 plus patches.</li>
</ul>

</div><h2 id="v1.7.3.1-preview20101002" nr="171" class="collapsible"> Changes in v1.7.3.1-preview20101002<br /><small>since 1.7.2.3-preview20100911</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.7.3.1 plus patches.</li>
<li>Updated to Vim 7.3, file-5.04 and InnoSetup 5.3.11</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Issue 528 (remove uninstaller from Start Menu) was fixed</li>
<li>Issue 527 (failing to find the certificate authority bundle) was fixed</li>
<li>Issue 524 (remove broken and unused <code>sdl-config</code> file) was fixed</li>
<li>Issue 523 (crash pushing to WebDAV remote) was fixed</li>
</ul>

</div><h2 id="v1.7.2.3-preview20100911" nr="172" class="collapsible"> Changes in v1.7.2.3-preview20100911<br /><small>since 1.7.1-preview20100612</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.7.2.3 plus patches.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Issue 519 (build problem with <code>compat/regex/regexec.c</code>) was fixed</li>
<li>Issue 430 (size of panes not preserved in <code>git-gui</code>) was fixed</li>
<li>Issue 411 (<code>git init</code> failing to work with CIFS paths) was fixed</li>
<li>Issue 501 (failing to clone repo from root dir using relative path) was fixed</li>
</ul>

</div><h2 id="v1.7.1-preview20100612" nr="173" class="collapsible"> Changes in v1.7.1-preview20100612<br /><small>since 1.7.0.2-preview20100309</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with Git 1.7.1 plus patches.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Issue 27 (<code>git-send-mail</code> not working properly) was fixed again</li>
<li>Issue 433 (error while running <code>git svn fetch</code>) was fixed</li>
<li>Issue 427 (Gitk reports error: "couldn't compile regular expression pattern: invalid repetition count(s)") was fixed</li>
<li>Issue 192 (output truncated) was fixed again</li>
<li>Issue 365 (Out of memory? mmap failed) was fixed</li>
<li>Issue 387 (gitk reports "error: couldn't execute "git:" file name too long") was fixed</li>
<li>Issue 409 (checkout of large files to network drive fails on XP) was fixed</li>
<li>Issue 428 (The return value of <code>git.cmd</code> is not the same as <code>git.exe</code>) was fixed</li>
<li>Issue 444 (Git Bash Here returns a "File not found error" in Windows 7 Professional - 64 bits) was fixed</li>
<li>Issue 445 (<code>git help</code> does nothing) was fixed</li>
<li>Issue 450 (<code>git --bare init</code> shouldn't set the directory to hidden.) was fixed</li>
<li>Issue 456 (git script fails with error code 1) was fixed</li>
<li>Issue 469 (error launch wordpad in last netinstall) was fixed</li>
<li>Issue 474 (<code>git update-index --index-info</code> silently does nothing) was fixed</li>
<li>Issue 482 (Add documentation to avoid "fatal: $HOME not set" error) was fixed</li>
<li>Issue 489 (<code>git.cmd</code> issues warning if <code>%COMSPEC%</code> has spaces in it) was fixed</li>
<li>Issue 436 (<code>mkdir : No such file or directory</code> error while using git-svn to fetch or rebase) was fixed</li>
<li>Issue 440 (Uninstall does not remove cheetah.) was fixed</li>
<li>Issue 441 (Git-1.7.0.2-preview20100309.exe installer fails with unwritable <code>msys-1.0.dll</code> when <code>ssh-agent</code> is running) was fixed</li>
</ul>

</div><h2 id="v1.7.0.2-preview20100309" nr="174" class="collapsible"> Changes in v1.7.0.2-preview20100309<br /><small>since 1.6.5.1-preview20091022</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with official Git 1.7.0.2.</li>
<li>Comes with Git-Cheetah (on 32-bit Windows only, for now).</li>
<li>Comes with connect.exe, a SOCKS proxy.</li>
<li>Tons of improvements in the installer, thanks to Sebastian Schuberth.</li>
<li>On Vista, if possible, symlinks are used for the built-ins.</li>
<li>Features Hany's <code>dos2unix</code> tool, thanks to Sebastian Schuberth.</li>
<li>Updated Tcl/Tk to version 8.5.8 (thanks Pat Thoyts!).</li>
<li>By default, only <code>.git/</code> is hidden, to work around a bug in Eclipse (thanks to Erik Faye-Lund).</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Fixed threaded grep (thanks to Heiko Voigt).</li>
<li><code>git gui</code> was fixed for all kinds of worktree-related failures (thanks Pat Thoyts).</li>
<li><code>git gui</code> now fully supports themed widgets (thanks Pat Thoyts and Heiko Voigt).</li>
<li>Git no longer complains about an unset <code>RUNTIME_PREFIX</code> (thanks Johannes Sixt).</li>
<li><code>git gui</code> can Explore Working Copy on Windows again (thanks Markus Heidelberg).</li>
<li><code>git gui</code> can create shortcuts again (fixes issue 425, thanks Heiko Voigt).</li>
<li>When <code>git checkout</code> cannot overwrite files because they are in use, it will offer to try again, giving the user a chance to release the file (thanks Heiko Voigt).</li>
<li>Ctrl+W will close <code>gitk</code> (thanks Jens Lehmann).</li>
<li><code>git gui</code> no longer binds Ctrl+C, which caused problems when trying to use said shortcut for the clipboard operation "Copy" (fixes issue 423, thanks Pat Thoyts).</li>
<li><code>gitk</code> does not give up when the command line length limit is reached (issue 387).</li>
<li>The exit code is fixed when <code>Git.cmd</code> is called from <code>cmd.exe</code> (thanks Alexey Borzenkov).</li>
<li>When launched via the (non-Cheetah) shell extension, the window icon is now correct (thanks Sebastian Schuberth).</li>
<li>Uses a TrueType font for the console, to be able to render UTF-8 correctly.</li>
<li>Clarified the installer's line ending options (issue 370).</li>
<li>Substantially speeded up startup time from cmd unless <code>NO_FSTAB_THREAD</code> is set (thanks Johannes Sixt).</li>
<li>Update <code>msys-1.0.dll</code> yet again, to handle quoted parameters better (thanks Heiko Voigt).</li>
<li>Updated cURL to a version that supports SSPI.</li>
<li>Updated tar to handle the pax headers generated by git archive.</li>
<li>Updated sed to a version that can handle the filter-branch examples.</li>
<li><code>.git*</code> files can be associated with the default text editor (issue 397).</li>
</ul>

</div><h2 id="v1.6.5.1-preview20091022" nr="175" class="collapsible"> Changes in v1.6.5.1-preview20091022<br /><small>since 1.6.4-preview20090729</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with official git 1.6.5.1.</li>
<li>Thanks to Johan 't Hart, files and directories starting with a single dot (such as <code>.git</code>) will now be marked hidden (you can disable this setting with core.hideDotFiles=false in your config) (Issue 288).</li>
<li>Thanks to Thorvald Natvig, Git on Windows can simulate symbolic links by using reparse points when available.  For technical reasons, this only works for symbolic links pointing to files, not directories.</li>
<li>A lot of work has been put into making it possible to compile Git's source code (the part written in C, of course, not the scripts) with Microsoft Visual Studio.  This work is ongoing.</li>
<li>Thanks to Sebastian Schuberth, we only offer the (Tortoise)Plink option in the installer if the presence of Plink was detected and at least one Putty session was found..</li>
<li>Thanks to Sebastian Schuberth, the installer has a nicer icon now.</li>
<li>Some more work by Sebastian Schuberth was done on better integration of Plink (Issues 305 &amp; 319).</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Thanks to Sebastian Schuberth, <code>git svn</code> picks up the SSH setting specified with the installer (Issue 305).</li>
</ul>

</div><h2 id="v1.6.4-preview20090729" nr="176" class="collapsible"> Changes in v1.6.4-preview20090729<br /><small>since 1.6.3.2-preview20090608</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with official git 1.6.4.</li>
<li>Supports https:// URLs, thanks to Erik Faye-Lund.</li>
<li>Supports <code>send-email</code>, thanks to Erik Faye-Lund (Issue 27).</li>
<li>Updated Tcl/Tk to version 8.5.7, thanks to Pat Thoyts.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>The home directory is now discovered properly (Issues 108 &amp; 259).</li>
<li>IPv6 is supported now, thanks to Martin Martin Storsjö (Issue 182).</li>
</ul>

</div><h2 id="v1.6.3.2-preview20090608" nr="177" class="collapsible"> Changes in v1.6.3.2-preview20090608<br /><small>since 1.6.3-preview20090507</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with official git 1.6.3.2.</li>
<li>Uses TortoisePlink instead of Plink if available.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Plink errors out rather than hanging when the user needs to accept a host key first (Issue 96).</li>
<li>The user home directory is inferred from <code>$HOMEDRIVE\$HOMEPATH</code> instead of <code>$HOME</code> (Issue 108).</li>
<li>The environment setting <code>$CYGWIN=tty</code> is ignored (Issues 138, 248 and 251).</li>
<li>The <code>ls</code> command shows non-ASCII filenames correctly now (Issue 188).</li>
<li>Adds more syntax files for vi (Issue 250).</li>
<li><code>$HOME/.bashrc</code> is included last from <code>/etc/profile</code>, allowing <code>.bashrc</code> to override all settings in <code>/etc/profile</code> (Issue 255).</li>
<li>Completion is case-insensitive again (Issue 256).</li>
<li>The <code>start</code> command can handle arguments with spaces now (Issue 258).</li>
<li>For some Git commands (such as <code>git commit</code>), <code>vi</code> no longer "restores" the cursor position.</li>
</ul>

</div><h2 id="v1.6.3-preview20090507" nr="178" class="collapsible"> Changes in v1.6.3-preview20090507<br /><small>since 1.6.2.2-preview20090408</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with official git 1.6.3.</li>
<li>Thanks to Marius Storm-Olsen, Git has a substantially faster <code>readdir()</code> implementation now.</li>
<li>Marius Storm-Olsen also contributed a patch to include <code>nedmalloc</code>, again speeding up Git noticably.</li>
<li>Compiled with GCC 4.4.0</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Portable Git contains a <code>README.portable</code>.</li>
<li>Portable Git now actually includes the builtins.</li>
<li>Portable Git includes <code>git-cmd.bat</code> and <code>git-bash.bat</code>.</li>
<li>Portable Git is now shipped as a <code>.7z</code>; it still is a self-extracting archive if you rename it to <code>.exe</code>.</li>
<li>Git includes the Perl Encode module now.</li>
<li>Git now includes the <code>filter-branch</code> tool.</li>
<li>There is a workaround for a Windows 7 regression triggering a crash in the progress reporting (e.g. during a clone). This fixes issues 236 and 247.</li>
<li><code>gitk</code> tries not to crash when it is closed while reading references (Issue 125, thanks Pat Thoyts).</li>
<li>In some setups, hard-linking is not as reliable as it should be, so we have a workaround which avoids hard links in some situations (Issues 222 and 229).</li>
<li><code>git-svn</code> sets <code>core.autocrlf</code> to <code>false</code> now, hopefully shutting up most of the <code>git-svn</code> reports.</li>
</ul>

</div><h2 id="v1.6.2.2-preview20090408" nr="179" class="collapsible"> Changes in v1.6.2.2-preview20090408<br /><small>since 1.6.2.1-preview20090322</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with official git 1.6.2.2.</li>
<li>Upgraded Tcl/Tk to 8.5.5.</li>
<li>TortoiseMerge is supported by mergetool now.</li>
<li>Uses pthreads (faster garbage collection on multi-core machines).</li>
<li>The test suite passes!</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Renaming was made more robust (due to Explorer or some virus scanners, files could not be renamed at the first try, so we have to try multiple times).</li>
<li>Johannes Sixt made lots of changes to the test-suite to identify properly which tests should pass, and which ones cannot pass due to limitations of the platform.</li>
<li>Support <code>PAGER</code>s with spaces in their filename.</li>
<li>Quite a few changes were undone which we needed in the olden days of msysGit.</li>
<li>Fall back to <code>/</code> when HOME cannot be set to the real home directory due to locale issues (works around Issue 108 for the moment).</li>
</ul>

</div><h2 id="v1.6.2.1-preview20090322" nr="180" class="collapsible"> Changes in v1.6.2.1-preview20090322<br /><small>since 1.6.2-preview20090308</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with official git 1.6.2.1.</li>
<li>A portable application is shipped in addition to the installer (Issue 195).</li>
<li>Comes with a Windows-specific <code>mmap()</code> implementation (Issue 198).</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>ANSI control characters are no longer shown verbatim (Issue 124).</li>
<li>Temporary files are created respecting <code>core.autocrlf</code> (Issue 177).</li>
<li>The Git Bash prompt is colorful again (Issue 199).</li>
<li>Fixed crash when hardlinking during a clone failed (Issue 204).</li>
<li>An infinite loop was fixed in <code>git-gui</code> (Issue 205).</li>
<li>The ssh protocol is always used with <code>plink.exe</code> (Issue 209).</li>
<li>More vim files are shipped now, so that syntax highlighting works.</li>
</ul>

</div><h2 id="v1.6.2-preview20090308" nr="181" class="collapsible"> Changes in v1.6.2-preview20090308<br /><small>since 1.6.1-preview20081225</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with official git 1.6.2.</li>
<li>Comes with upgraded vim 7.2.</li>
<li>Compiled with GCC 4.3.3.</li>
<li>The user can choose the preferred CR/LF behavior in the installer now.</li>
<li>Peter Kodl contributed support for hardlinks on Windows.</li>
<li>The bash prompt shows information about the current repository.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>If supported by the file system, pack files can grow larger than 2gb.</li>
<li>Comes with updated <code>msys-1.0.dll</code> (should fix some Vista issues).</li>
<li>Assorted fixes to support the new <code>libexec/git-core/</code> layout better.</li>
<li>Read-only files can be properly replaced now.</li>
<li><code>git-svn</code> is included again (original caveats still apply).</li>
<li>Obsolete programs from previous installations are cleaned up.</li>
</ul>

</div><h2 id="v1.6.1-preview20081225" nr="182" class="collapsible"> Changes in v1.6.1-preview20081225<br /><small>since 1.6.0.2-preview20080923</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with official git 1.6.1.</li>
<li>Avoid useless console windows.</li>
<li>Installer remembers how to handle PATH.</li>
</ul>

</div><h2 id="v1.6.0.2-preview20080923" nr="183" class="collapsible"> Changes in v1.6.0.2-preview20080923<br /><small>since 1.6.0.2-preview20080921</h2></small><div>

<h3>Bugfixes</h3>

<ul>
<li>ssh works again.</li>
<li><code>git add -p</code> works again.</li>
<li>Various programs that aborted with <code>Assertion failed: argv0_path</code> are fixed.</li>
</ul>

</div><h2 id="v1.6.0.2-preview20080921" nr="184" class="collapsible"> Changes in v1.6.0.2-preview20080921<br /><small>since 1.5.6.1-preview20080701</h2></small><div>

<ul>
<li>Removed Features</li>
<li><code>git svn</code> is excluded from the end-user installer (see Known Issues).</li>
</ul>

<h3>New Features</h3>

<ul>
<li>Comes with official git 1.6.0.2.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>No Windows-specific bugfixes.</li>
</ul>

</div><h2 id="v1.5.6.1-preview20080701" nr="185" class="collapsible"> Changes in v1.5.6.1-preview20080701<br /><small>since 1.5.6-preview20080622</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with official git 1.5.6.1.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Includes fixed <code>msys-1.0.dll</code> that supports Vista and Windows Server 2008 (Issue 122).</li>
<li>cmd wrappers do no longer switch off echo.</li>
</ul>

</div><h2 id="v1.5.6-preview20080622" nr="186" class="collapsible"> Changes in v1.5.6-preview20080622<br /><small>since 1.5.5-preview20080413</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with official git 1.5.6.</li>
<li>Installer supports configuring a user provided Plink (PuTTY).</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Comes with tweaked <code>msys-1.0.dll</code> to solve some command line mangling issues.</li>
<li>cmd wrapper does no longer close the command window.</li>
<li>Programs in the system <code>PATH</code>, for example editors, can be launched from Git without specifying their full path.</li>
<li><code>git stash apply stash@{1}</code> works.</li>
<li>Comes with basic ANSI control code emulation for the Windows console to avoid wrapping of pull/merge's diffstats.</li>
<li>Git correctly passes port numbers to PuTTY's Plink</li>
</ul>

</div><h2 id="v1.5.5-preview20080413" nr="187" class="collapsible"> Changes in v1.5.5-preview20080413<br /><small>since 1.5.4-preview20080202</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with official git 1.5.5.</li>
<li><code>core.autocrlf</code> is enabled (<code>true</code>) by default. This means git converts to Windows line endings (CRLF) during checkout and converts to Unix line endings (LF) during commit. This is the right choice for cross-platform projects. If the conversion is not reversible, git warns the user. The installer warns about the new default before the installation starts.</li>
<li>The user does no longer have to "accept" the GPL but only needs to press "continue".</li>
<li>Installer deletes shell scripts that have been replaced by builtins. Upgrading should be safer.</li>
<li>Supports <code>git svn</code>. Note that the performance might be below your expectation.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Newer ssh fixes connection failures (issue 74).</li>
<li>Comes with MSys-1.0.11-20071204.  This should solve some "fork: resource unavailable" issues.</li>
<li>All DLLs are rebased to avoid problems with "fork" on Vista.</li>
</ul>

</div><h2 id="v1.5.4-preview20080202" nr="188" class="collapsible"> Changes in v1.5.4-preview20080202<br /><small>since 1.5.3.6-preview20071126</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Comes with official git 1.5.4.</li>
<li>Some commands that are not yet suppoted on Windows are no longer included (see Known Issues above).</li>
<li>Release notes are displayed in separate window.</li>
<li>Includes <code>qsort</code> replacement to improve performance on Windows 2000.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Fixes invalid error message that setup.ini cannot be deleted on uninstall.</li>
<li>Setup tries harder to finish the installation and reports more detailed errors.</li>
<li>Vim's syntax highlighting is suitable for dark background.</li>
</ul>

</div><h2 id="v1.5.3.6-preview20071126" nr="189" class="collapsible"> Changes in v1.5.3.6-preview20071126<br /><small>since 1.5.3.5-preview20071114</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Git is included in version 1.5.3.6.</li>
<li>Setup displays release notes.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li><code>pull</code>/<code>fetch</code>/<code>push</code> in <code>git-gui</code> works. Note, there is no way for <code>ssh</code> to ask for a passphrase or for confirmation if you connect to an unknown host. So, you must have ssh set up to work without passphrase. Either you have a key without passphrase, or you started ssh-agent. You may also consider using PuTTY by pointing <code>GIT_SSH</code> to <code>plink.exe</code> and handle your ssh keys with Pageant. In this case you should include your login name in urls. You must also connect to an unknown host once from the command line and confirm the host key, before you can use it from <code>git-gui</code>.</li>
</ul>

</div><h2 id="v1.5.3.5-preview20071114" nr="190" class="collapsible"> Changes in v1.5.3.5-preview20071114<br /><small>since 1.5.3-preview20071027</h2></small><div>

<h3>New Features</h3>

<ul>
<li>Git is included in version 1.5.3.5.</li>
<li>Setup can be installed as normal user.</li>
<li>When installing as Administrator, all icons except the Quick Launch icon will be created for all users.</li>
<li><code>git help user-manual</code> displays the user manual.</li>
</ul>

<h3>Bugfixes</h3>

<ul>
<li>Git Bash works on Windows XP 64.</li>
</ul>

</div><h2 id="v1.5.3-preview20071027" nr="191" class="collapsible"> Changes in v1.5.3-preview20071027<br /><small>since 1.5.3-preview20071019</h2></small><div>

<h3>Bugfixes</h3>

<ul>
<li>The templates for a new repository are found.</li>
<li>The global configuration <code>/etc/gitconfig</code> is found.</li>
<li>Git Gui localization works. It falls back to English if a translation has errors.</li>
</ul>

</div><h2 id="v1.5.3-preview20071019" nr="192" class="collapsible"> Changes since WinGit-0.2-alpha</h2><div>

<ul>
<li>The history of the release notes stops here. Various new features and bugfixes are available since WinGit-0.2-alpha. Please check the git history of the msysgit project for details.</li>
</ul>
</div>
</div>
<script>
(() => {
const hideEl = window.location.hash && window.location.hash != '#latest' ?
(el) => "#" + el.id !== window.location.hash :
(el) => el.getAttribute('nr') !== '1';
for (let el of document.getElementsByClassName('collapsible')) {
let arrow = document.createElement('div');
arrow.innerHTML = '▽';
arrow.style.float = 'left';
arrow.style.position = 'relative';
arrow.style.left = '-1em';
arrow.style.top = '+1.5em';
arrow.style.fontSize = 'larger';
arrow.style.cursor = 'pointer';

const toggle = () => {
// this.classList.toggle('active');
let details = el.nextElementSibling;
if (details.style.display === 'none') {
details.style.display = 'block';
arrow.innerHTML = '▽';
} else {
details.style.display = 'none';
arrow.innerHTML = '▷';
}
};

if (hideEl(el)) {
toggle();
}

el.addEventListener('click', toggle);
arrow.addEventListener('click', toggle);
el.parentElement.insertBefore(arrow, el);
}
})();
</script>
</body>
</html>

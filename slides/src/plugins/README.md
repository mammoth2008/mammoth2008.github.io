Impress.js Plugins documentation
================================

The default set of plugins
--------------------------

A lot of impress.js features are and will be implemented as plugins. Each plugin
has user documentation in a README.md file in [its own directory](./).

The plugins in this directory are called default plugins, and - unsurprisingly -
are enabled by default. However, most of them won't do anything by default, 
rather require the user to invoke them somehow. For example:

* The *navigation* plugin waits for the user to press some keys, arrows, page
  down, page up, space or tab.
* The *autoplay* plugin looks for the HTML attribute `data-autoplay` to see
  whether it should do its thing. It can also be triggered with a URL GET parameter
  `?impress-autoplay=5` *5 is the waiting duration*. 
* The *toolbar* plugin looks for a `<div>` element to become visible.

Extra addons
------------

Yet more features are available in presentations that enable 
[extra addons](https://github.com/impress/impress-extras). Extra addons are 3rd party plugins 
that are not part of impress.js, but that we have nevertheless collected together into the 
impress-extras repo to provide convenient and standardized access to them. To include 
the extra addons when checking out impress.js, use git clone --recursive. Even then, they 
are not activated by default in a presentation, rather each must be included with their own `<script>` tag.

Note: The enabled extra addons are automatically initialized by the *extras*
plugin.

Example HTML and CSS
--------------------

Generally plugins will do something sane, or nothing, by default. Hence, no
particular HTML or CSS is required. The README file of each plugin documents the
HTML and CSS that you can use with that plugin.

For your convenience, below is some sample HTML and CSS code covering all the
plugins that you may want to use or adapt.

Additional parameters for addons
--------------------------------

Some addons can handle additional HTML data attributes to help us in further customization:
- Markdown-JS: You can pass a specific Markdown dialect to the plugin using `data-markdown-dialect="Another Dialect"`.

### Sample HTML to enable plugins and extra addons

    <head>
      <!-- CSS files if using Highlight.js or Mermaid.js extras. -->
      <link rel="stylesheet" href="../../extras/highlight/styles/github.css">
      <link rel="stylesheet" href="../../extras/mermaid/mermaid.forest.css">
    </head>
    <body>
      <div id="impress" data-autoplay="10">
        <div class="step"
             data-autoplay="15"
             data-rel-x="1000"
             data-rel-y="1000">

          <h1>Slide content</h1>
          
          <ul>
            <li class="substep">Point 1</li>
            <li class="substep">Point 2</li>
          </ul>

          <div class="notes">
          Speaker notes are shown in the impressConsole.
          </div>
        </div>
      </div>
      
      <div id="impress-toolbar"></div>
      <div class="impress-progressbar"><div></div></div>
      <div class="impress-progress"></div>
      <div id="impress-help"></div>

      <script type="text/javascript" src="../../extras/highlight/highlight.pack.js"></script>
      <script type="text/javascript" src="../../extras/mermaid/mermaid.min.js"></script>
      <script type="text/javascript" src="../../extras/markdown/markdown.js"></script>
      <script type="text/javascript" src="../../extras/mathjax/tex-chtml-full.js"></script>
    </body>

### Sample CSS related to plugins and extra addons

The sample css related to plugins and extra addons is located in [css/impress-common.css](../../css/impress-common.css).

For developers
==============

The vision for impress.js is to provide a compact core library doing the
actual presentations, with a collection of plugins that provide additional
functionality. A default set of plugins are distributed together with the core 
impress.js, and are located in this directory. They are called *default plugins*
because they are distributed and active when users use the [js/impress.js](../../js/impress.js)
in their presentations.

Building js/impress.js
-----------------------

The common way to use impress.js is to link to the file 
[js/impress.js](../../js/impress.js). This is a simple concatenation of the 
core impress.js and all plugins in this directory. If you edit or add code 
under [src/](../), you can run `node build.js` to recreate the distributable
`js/impress.js` file. The build script also creates a minified file, but this
is not included in the git repository.

### Tip: Build errors

If your code has parse errors, the `build.js` will print a rather unhelpful
exception like

    /home/hingo/hacking/impress.js/js/impress.js

    /home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:271
        throw new JS_Parse_Error(message, line, col, pos);
              ^
    Error
        at new JS_Parse_Error (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:263:18)
        at js_error (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:271:11)
        at croak (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:733:9)
        at token_error (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:740:9)
        at unexpected (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:746:9)
        at Object.semicolon [as 1] (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:766:43)
        at prog1 (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:1314:21)
        at simple_statement (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:906:27)
        at /home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:814:19
        at block_ (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:1003:20)

You will be pleased to know, that the concatenation of the unminified file
[js/impress.js](../../js/impress.js) has already succeeded at this point. Just
open a test in your browser, and the browser will show you the line and error.


### Structure, naming and policy

Each plugin is contained within its own directory. The name of the directory
is the name of the plugin. For example, imagine a plugin called *pluginA*:

    src/plugins/plugina/

The main javascript file should use the directory name as its root name:

    src/plugins/plugina/plugina.js

For most plugins, a single `.js` file is enough.

Note that the plugin name is also used as a namespace for various things. For
example, the *autoplay* plugin can be configured by setting the `data-autoplay="5"`
attribute on a `div`.

As a general rule ids, classes and attributes within the `div#impress` root
element, may use the plugin name directly (e.g. `data-autoplay="5"`). However,
outside of the root element, you should use `impress-pluginname` (e.g.
`<div id="impress-toolbar">`. The latter (longer) form also applies to all
events, they should be prefixed with `impress:pluginname`.

You should use crisp and descriptive names for your plugins. But
sometimes you might optimize for a short namespace. Hence, the
[Relative Positioning Plugin](rel/rel.js) is called `rel` to keep html attributes
short. You should not overuse this idea!

Note that for default plugins, which is all plugins in this directory,
**NO css, html or image files** are allowed.

Default plugins must not add any global variables.

### Testing

The plugin directory should also include tests, which should use the *QUnit* and
*Syn* libraries under [test/](../../test). You can have as many tests as you like,
but it is suggested your first and main test file is called `plugina_tests.html`
and `plugina_tests.js` respectively. You need to add your test `.js` file into
[/qunit_test_runner.html](../../qunit_test_runner.html), and the `.js` file 
should start by loading the test `.html` file into the 
`iframe#presentation-iframe`. See [navigation-ui](navigation-ui) plugin for an 
example.

You are allowed to test your plugin whatever way you like, but the general
approach is for the test to load the [js/impress.js](../../js/impress.js) file
produced by build.js. This way you are testing what users will actually be
using, rather than the uncompiled source code.

HowTo write a plugin
--------------------

### Encapsulation

To avoid polluting the global namespace, plugins must encapsulate them in the
standard javascript anonymous function:

    /**
     * Plugin A - An example plugin
     *
     * Description...
     *
     * Copyright 2016 Firstname Lastname, email or github handle
     * Released under the MIT license.
     */
    (function ( document, window ) {

        // Plugin implementation...

    })(document, window);


### Init plugins

We categorize plugins into various categories, based on how and when they are 
called, and what they do.

An init plugin is the simplest kind of plugin. It simply listens for the
`impress().init()` method to send the `impress:init` event, at which point
the plugin can initialize itself and start doing whatever it does, for example 
by calling methods in the public api returned by `impress()`.

The `impress:init` event has the `div#impress` element as its `target` attribute,
whereas `event.detail.api` contains the same object that is returned by calling
`impress()`. It is customary to store the api object sent by the event rather than
calling `impress()` from the global namespace.

Example:

    /**
     * Plugin A - An example plugin
     *
     * Description...
     *
     * Copyright 2016 Firstname Lastname, email or github handle
     * Released under the MIT license.
     */
    (function ( document, window ) {
        var root;
        var api;
        var lib;

        document.addEventListener( "impress:init", function( event ) {
            root = event.target;
            api = event.detail.api;
            lib = api.lib;

            // Element attributes starting with "data-", become available under
            // element.dataset. In addition hyphenized words become camelCased.
            var data = root.dataset;
            // Get value of `<div id="impress" data-plugina-foo="...">`
            var foo = data.pluginaFoo;
            // ...
        }
    })(document, window);


Both [Navigation](navigation/navigation.js) and [Autoplay](autoplay/autoplay.js)
are init plugins.

To provide end user configurability in your plugin, a good idea might be to
read html attributes from the impress presentation. The
[Autoplay](autoplay/autoplay.js) plugin does exactly this, you can provide
a default value in the `div#impress` element, or in each `div.step`.

A plugin must only use html attributes in its designated namespace, which is

    data-pluginName-*="value"

For example, if *pluginA* offers config options `foo` and `bar`, it would look
like this:

    <div id="impress" data-plugina-foo="5" data-plugina-bar="auto" >


### Pre-init plugins

Some plugins need to run before even impress().init() does anything. These
are typically *filters*: they want to modify the html via DOM calls, before
impress.js core parses the presentation. We call these *pre-init plugins*.

A pre-init plugin must be called synchronously, before `impress().init()` is
executed. Plugins can register themselves to be called in the pre-init phase
by calling:

    impress.addPreInitPlugin( plugin [, weight] );

The argument `plugin` must be a function. `weight` is optional and defaults to
`10`. Plugins are ordered by weight when they are executed, with lower weight
first.

The [Relative Positioning Plugin](rel/rel.js) is an example of a pre-init plugin.

### Pre-StepLeave plugins

A *pre-stepleave plugin* is called synchronously from impress.js core at the
beginning of `impress().goto()`. 

To register a plugin, call

    impress.addPreStepLeavePlugin( plugin [, weight] );

When the plugin function is executed, it will be passed an argument
that resembles the `event` object from DOM event handlers:

`event.target` contains the current step, which we are about to leave. 

`event.detail.next` contains the element we are about to transition to.

`event.detail.reason` contains a string, one of "next", "prev" or "goto",
which tells you which API function was called to initiate the transition.

`event.detail.transitionDuration` contains the transitionDuration for the 
upcoming transition.

A pre-stepleave plugin may alter the values in `event.detail` (except for 
`reason`), and this can change the behavior of the upcoming transition.
For example, the `goto` plugin will set the `event.detail.next` to point to
some other element, causing the presentation to jump to that step instead. 


### GUI plugins

A *GUI plugin* is actually just an init plugin, but is a special category that
exposes visible widgets or effects in the presentation. For example, it might
provide clickable buttons to go to the next and previous slide. 

Note that all plugins shipped in the default set **must not** produce any visible
html elements unless the user asks for it. A recommended best practice is to let 
the user add a div element, with an id equaling the plugin's namespace, in the 
place where he wants to see whatever visual UI elements the plugin is providing:

    <div id="impress-plugina"></div>

Another way to show the elements of a UI plugin might be by allowing the user
to explicitly press a key, like "H" for a help dialog.

[Toolbar plugin](toolbar/README.md) is an example of a GUI plugin. It presents
a toolbar where other plugins can add their buttons in a centralized fashion.

Remember that for default plugins, even GUI plugins, no html files, css files
or images are allowed. Everything must be generated from javascript. The idea
is that users can theme widgets with their own CSS. (A plugin is of course welcome
to provide example CSS that can be copypasted :-)

Dependencies
------------

If *pluginB* depends on the existence of *pluginA*, and also *pluginA* must run 
before *pluginB*, then *pluginB* should not listen to the `impress:init` event, 
rather *pluginA* should send its own init event, which *pluginB* listens to.

Example:

    // pluginA
    document.addEventListener("impress:init", function (event) {
        // plugin A does it's own initialization first...

        // Signal other plugins that plugin A is now initialized
        var root = document.querySelector( "div#impress" );
        var event = document.createEvent("CustomEvent");
        event.initCustomEvent("impress:plugina:init', true, true, { "plugina" : "data..." });
        root.dispatchEvent(event);
    }, false);
    
    // pluginB
    document.addEventListener("impress:plugina:init", function (event) {
        // plugin B implementation
    }, false);

A plugin should use the namespace `impress:pluginname:*` for any events it sends.

In theory all plugins could always send an `init` and other events, but in
practice we're adding them on an as needed basis.

Impress.js 插件文档
=====================

默认插件集
----------

impress.js 的许多功能将以插件的形式实现。每个插件的用户文档都在 [其自己的目录](./) 中的 README.md 文件中。

此目录中的插件称为默认插件，并且默认情况下启用。然而，大多数插件在默认情况下不会执行任何操作，而是需要用户以某种方式调用它们。例如：

* **navigation** 插件等待用户按下某些键，例如箭头键、Page Down、Page Up、空格或 Tab 键。
* **autoplay** 插件查找 HTML 属性 `data-autoplay` 以确定是否应该执行其功能。它还可以通过 URL GET 参数 `?impress-autoplay=5` 触发，其中 5 是等待时间。
* **toolbar** 插件查找一个 `<div>` 元素以显示。

额外的插件
----------

启用 [额外插件](https://github.com/impress/impress-extras) 的演示文稿中还可以使用更多功能。额外插件是非 impress.js 的第三方插件，但我们将它们收集到 impress-extras 仓库中，以便提供方便和标准化的访问方式。要在检出 impress.js 时包括额外插件，请使用 `git clone --recursive`。即便如此，它们在演示文稿中默认未激活，而是每个都必须通过自己的 `<script>` 标签包含。

注意：启用的额外插件会自动由 **extras** 插件初始化。

示例 HTML 和 CSS
----------------

一般来说，插件会默认执行一些合理的操作，或者默认不做任何事情。因此，不需要特定的 HTML 或 CSS。每个插件的 README 文件记录了可以与该插件一起使用的 HTML 和 CSS。

为方便起见，下面是一些示例 HTML 和 CSS 代码，涵盖了您可能希望使用或调整的所有插件。

附加参数
--------

某些插件可以处理附加的 HTML 数据属性，以帮助进一步定制：
- Markdown-JS：您可以使用 `data-markdown-dialect="Another Dialect"` 向插件传递特定的 Markdown 方言。

### 启用插件和额外插件的示例 HTML

```html
<head>
  <!-- 如果使用 Highlight.js 或 Mermaid.js 额外插件的 CSS 文件 -->
  <link rel="stylesheet" href="../../extras/highlight/styles/github.css">
  <link rel="stylesheet" href="../../extras/mermaid/mermaid.forest.css">
</head>
<body>
  <div id="impress" data-autoplay="10">
    <div class="step"
         data-autoplay="15"
         data-rel-x="1000"
         data-rel-y="1000">

      <h1>幻灯片内容</h1>
      
      <ul>
        <li class="substep">要点 1</li>
        <li class="substep">要点 2</li>
      </ul>

      <div class="notes">
      演讲者笔记将在 impressConsole 中显示。
      </div>
    </div>
  </div>
  
  <div id="impress-toolbar"></div>
  <div class="impress-progressbar"><div></div></div>
  <div class="impress-progress"></div>
  <div id="impress-help"></div>

  <script type="text/javascript" src="../../extras/highlight/highlight.pack.js"></script>
  <script type="text/javascript" src="../../extras/mermaid/mermaid.min.js"></script>
  <script type="text/javascript" src="../../extras/markdown/markdown.js"></script>
  <script type="text/javascript" src="../../extras/mathjax/tex-chtml-full.js"></script>
</body>
```

### 插件和额外插件相关的示例 CSS

插件和额外插件相关的示例 CSS 位于 [css/impress-common.css](../../css/impress-common.css)。

对于开发者
==========

impress.js 的愿景是提供一个紧凑的核心库来执行实际演示，并通过一组插件提供附加功能。与核心 impress.js 一起分发的一组默认插件位于此目录中。它们称为 **默认插件**，因为用户在其演示中使用 [js/impress.js](../../js/impress.js) 时默认分发和激活。

构建 js/impress.js
-------------------

使用 impress.js 的常见方法是链接到文件 [js/impress.js](../../js/impress.js)。这是核心 impress.js 和此目录中所有插件的简单连接。如果您在 [src/](../) 目录下编辑或添加代码，可以运行 `node build.js` 来重新创建可分发的 `js/impress.js` 文件。构建脚本还会创建一个压缩文件，但此文件未包含在 git 仓库中。

### 提示：构建错误

如果您的代码有解析错误，`build.js` 将打印出一个相当无帮助的异常，如

```plaintext
/home/hingo/hacking/impress.js/js/impress.js

/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:271
    throw new JS_Parse_Error(message, line, col, pos);
          ^
Error
    at new JS_Parse_Error (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:263:18)
    at js_error (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:271:11)
    at croak (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:733:9)
    at token_error (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:740:9)
    at unexpected (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:746:9)
    at Object.semicolon [as 1] (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:766:43)
    at prog1 (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:1314:21)
    at simple_statement (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:906:27)
    at /home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:814:19
    at block_ (/home/hingo/hacking/impress.js/node_modules/uglify-js/lib/parse-js.js:1003:20)
```

您会高兴地知道，未压缩文件 [js/impress.js](../../js/impress.js) 的连接已经成功完成。只需在浏览器中打开测试，浏览器会显示错误的行和错误信息。

### 结构、命名和策略

每个插件都包含在其自己的目录中。目录的名称就是插件的名称。例如，假设有一个名为 **pluginA** 的插件：

```plaintext
src/plugins/plugina/
```

主 JavaScript 文件应使用目录名称作为其根名称：

```plaintext
src/plugins/plugina/plugina.js
```

对于大多数插件，单个 `.js` 文件就足够了。

请注意，插件名称还用作各种事物的命名空间。例如，可以通过在 `div` 上设置 `data-autoplay="5"` 属性来配置 **autoplay** 插件。

作为一般规则，`div#impress` 根元素内的 id、类和属性可以直接使用插件名称（例如 `data-autoplay="5"`）。然而，在根元素之外，您应该使用 `impress-pluginname`（例如 `<div id="impress-toolbar">`）。较长的形式也适用于所有事件，它们应以 `impress:pluginname` 为前缀。

您应该为插件使用清晰且描述性的名称。但有时您可能会为了一个简短的命名空间而优化名称。因此，[相对定位插件](rel/rel.js) 被称为 `rel` 以保持 HTML 属性简短。您不应过度使用这种做法！

请注意，对于默认插件，即此目录中的所有插件，**不允许使用 CSS、HTML 或图像文件**。

默认插件不得添加任何全局变量。

### 测试

插件目录还应包括使用 [test/](../../test) 下的 **QUnit** 和 **Syn** 库的测试。您可以有任意数量的测试，但建议您的第一个和主要的测试文件分别称为 `plugina_tests.html` 和 `plugina_tests.js`。您需要将测试 `.js` 文件添加到 [/qunit_test_runner.html](../../qunit_test_runner.html) 中，并且 `.js` 文件应以加载测试 `.html` 文件到 `iframe#presentation-iframe` 开始。请参阅 [navigation-ui](navigation-ui) 插件的示例。

您可以以任何喜欢的方式测试插件，但一般方法是让测试加载由 build.js 生成的 [js/impress.js](../../js/impress.js) 文件。这样您测试的是用户实际使用的内容，而不是未编译的源代码。

如何编写插件
--------------

### 封装

为了避免污染全局命名空间，插件必须封装在标准的 JavaScript 匿名函数中：

```javascript
/**
 * Plugin A - An

 example plugin
 *
 * Description...
 *
 * Copyright 2016 Firstname Lastname, email or github handle
 * Released under the MIT license.
 */
(function (document, window) {

    // Plugin implementation...

})(document, window);
```

### 初始化插件

我们将插件分类为各种类型，基于它们的调用方式和时间以及它们的功能。

初始化插件是最简单的插件类型。它只需监听 `impress().init()` 方法发送的 `impress:init` 事件，此时插件可以初始化并开始执行其功能，例如调用 `impress()` 返回的公共 API 中的方法。

`impress:init` 事件的 `target` 属性是 `div#impress` 元素，而 `event.detail.api` 包含与调用 `impress()` 返回的对象相同的对象。通常，将事件发送的 API 对象存储起来，而不是从全局命名空间调用 `impress()`。

示例：

```javascript
/**
 * Plugin A - An example plugin
 *
 * Description...
 *
 * Copyright 2016 Firstname Lastname, email or github handle
 * Released under the MIT license.
 */
(function (document, window) {
    var root;
    var api;
    var lib;

    document.addEventListener("impress:init", function(event) {
        root = event.target;
        api = event.detail.api;
        lib = api.lib;

        // 以 "data-" 开头的元素属性在 element.dataset 下可用。此外，连字符单词变为骆驼拼写。
        var data = root.dataset;
        // 获取 `<div id="impress" data-plugina-foo="...">` 的值
        var foo = data.pluginaFoo;
        // ...
    });
})(document, window);
```

[Navigation](navigation/navigation.js) 和 [Autoplay](autoplay/autoplay.js) 都是初始化插件。

为了在插件中提供终端用户可配置性，一个好主意是从 impress 演示中读取 HTML 属性。[Autoplay](autoplay/autoplay.js) 插件正是这样做的，您可以在 `div#impress` 元素或每个 `div.step` 中提供默认值。

插件必须仅在其指定的命名空间内使用 HTML 属性，即：

```html
data-pluginName-*="value"
```

例如，如果 **pluginA** 提供配置选项 `foo` 和 `bar`，它看起来应该是这样的：

```html
<div id="impress" data-plugina-foo="5" data-plugina-bar="auto"></div>
```

### 预初始化插件

有些插件需要在 impress().init() 执行任何操作之前运行。这些通常是 **过滤器**：它们希望通过 DOM 调用修改 HTML，在 impress.js 核心解析演示文稿之前。我们称这些为 **预初始化插件**。

预初始化插件必须在 `impress().init()` 执行之前同步调用。插件可以通过调用以下方法注册自己在预初始化阶段被调用：

```javascript
impress.addPreInitPlugin(plugin [, weight]);
```

参数 `plugin` 必须是一个函数。`weight` 是可选的，默认值为 `10`。插件按权重顺序执行，权重较低的先执行。

[相对定位插件](rel/rel.js) 是预初始化插件的一个示例。

### 预离开步骤插件

**预离开步骤插件** 在 impress.js 核心的 `impress().goto()` 开始时同步调用。

要注册插件，请调用

```javascript
impress.addPreStepLeavePlugin(plugin [, weight]);
```

当插件函数执行时，它将被传递一个类似于 DOM 事件处理程序的 `event` 对象：

`event.target` 包含当前步骤，我们即将离开。

`event.detail.next` 包含我们即将过渡到的元素。

`event.detail.reason` 包含一个字符串，值为 "next"、"prev" 或 "goto" 之一，表示调用哪个 API 函数来启动过渡。

`event.detail.transitionDuration` 包含即将过渡的过渡持续时间。

预离开步骤插件可以修改 `event.detail` 中的值（除 `reason` 外），这可以改变即将过渡的行为。例如，`goto` 插件会将 `event.detail.next` 设置为指向其他元素，从而导致演示跳转到该步骤。

### GUI 插件

**GUI 插件** 实际上只是一个初始化插件，但它是一个特殊类别，在演示文稿中暴露可见的控件或效果。例如，它可能提供可点击的按钮来进入下一张和上一张幻灯片。

请注意，默认插件集中的所有插件 **不得** 生成任何可见的 HTML 元素，除非用户要求。推荐的最佳实践是让用户在希望看到插件提供的任何可视化 UI 元素的位置添加一个 id 等于插件命名空间的 `div` 元素：

```html
<div id="impress-plugina"></div>
```

显示 UI 插件元素的另一种方法是允许用户显式按键，例如按 "H" 键显示帮助对话框。

[Toolbar 插件](toolbar/README.md) 是 GUI 插件的一个示例。它提供了一个工具栏，其他插件可以在其中添加它们的按钮，以集中方式管理。

请记住，对于默认插件，即使是 GUI 插件，不允许使用 HTML 文件、CSS 文件或图像。所有内容必须通过 JavaScript 生成。用户可以使用他们自己的 CSS 对小部件进行主题化。（当然，插件可以提供可以复制粘贴的示例 CSS。）

依赖项
------

如果 **pluginB** 依赖于 **pluginA** 的存在，并且 **pluginA** 必须在 **pluginB** 之前运行，那么 **pluginB** 不应监听 `impress:init` 事件，而是 **pluginA** 应发送自己的初始化事件，**pluginB** 监听该事件。

示例：

```javascript
// pluginA
document.addEventListener("impress:init", function (event) {
    // plugin A 先完成自己的初始化...

    // 向其他插件发出插件 A 已初始化的信号
    var root = document.querySelector("div#impress");
    var event = document.createEvent("CustomEvent");
    event.initCustomEvent("impress:plugina:init", true, true, { "plugina": "data..." });
    root.dispatchEvent(event);
}, false);
    
// pluginB
document.addEventListener("impress:plugina:init", function (event) {
    // plugin B 实现
}, false);
```

插件应使用命名空间 `impress:pluginname:*` 发送任何事件。

理论上所有插件都可以始终发送 `init` 和其他事件，但实际上我们根据需要添加它们。

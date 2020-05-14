<!--
https://ae01.alicdn.com/kf/Haf4d3b0529ba47669bf69c7bfc71a5f1Y.png
前端
javascript基础（一）
javascript的数据类型与变量的基础用法
javascript数据类型包括字符串、数组、对象等，还有一些高阶函数的使用
-->

## javascript基础（一）

> javascript的数据类型与变量的基础用法，javascript数据类型包括字符串、数组、对象等，还有一些高阶函数的使用

##### 字符串
包括模板字符串，操作字符串等
```javascript
`${"cza"}`
"cza".length
"cza"[0]
"cza".toUpperCase
"cza".toLowerCase
"cza".indexOf
"cza".substring
```

##### 数组
```javascript
Array.length
Array.indexOf
Array.push
Array.pop
Array.unshift
Array.shift
Array.sort
Array.reverse
Array.slice
Array.splice
Array.concat
Array.join
Array.forEach
Array.every
Array.map
Array.reduce
Array.filter
```

##### 对象
```javascript
'toString' in object
object.hasOwnProperty('property')
```

##### Map
初始化的时候需要一个二维数组，或者直接初始化为空
```javascript
map.set('cza', 123)
map.has('cza')
map.get('cza')
map.delete('cza')
```

##### Set
初始化的时候需要一个一维数组，或者直接初始化为空
```javascript
set.add('cza')
set.delete('cza')
```

遍历数组可以采用下标循环，但是Map和Set就无法使用下标，为了统一集合类型，引入iterable类型  
可以使用for-of来遍历，其中遍历Map的时候，是一个数组，包含key-value  

或者可以使用forEach来遍历元素，Set前两个参数都是元素本身， 因为没有索引，
而Map前两个参数分别表示value和key

通过arguments这个函数内生效的关键字，即使不定义参数，也可以拿到传入值  
块级作用域和常量，分别为let和const  
解构赋值
```javascript
var {name: newName, age: newAge} = person;
```

##### 正则
正则使用两个斜杠表示，可以在尾部添加g，表示全局搜索，即可以执行多次。还可以添加i，表示忽略大小写，m表示多行匹配
```javascript
/ABC\d/
new RegExp('ABC\d')
/(\d+)/.exec('cza100')
```

##### 浏览器对象
* window：不但充当全局作用域，且表示浏览窗口。如常用的innerHeight、innerWidth
* navigator：表示浏览器的信息，如：navigator.userAgent, .platform, appName
* screen：表示屏幕的信息
* location：表示当前页面的url信息，.pathname, .search，常用还有.assign()和.reload()
* document：当前DOM树的根节点
* history

```javascript
node = document.querySelector('#app');
node.children
node.firstElementChild
node.lastElementChild
```




## web.xml 文件中 context-param 中的 contextConfigLocation 与 init-param 中的 contextConfigLocation 的区别
* 有时候，会发现一个web.xml文件中，会配置两个 contextConfigLocation ，分别在 context-param 中和 servlet 中。如下
```xml
<web-app ...>
	<context-param>
		<param-name>contextConfigLocation</param-name>
		<param-value>classpath*:/aplicationContext.xml</param-value>
	</context-param>
	<listener>
		<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
	</listener>
    ...

    <servlet>
		<servlet-name>dispatcher</servlet-name>
		<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
		<init-param>
			<param-name>contextConfigLocation</param-name>
			<param-value>classpath*:/springmvc-context.xml</param-value>
		</init-param>
		<load-on-startup>1</load-on-startup>
	</servlet>
	<servlet-mapping>
		<servlet-name>dispatcher</servlet-name>
		<url-pattern>/</url-pattern>
	</servlet-mapping>
</web-app>
```

* context-param 和 init-param 区别
    * 主要是作用域不一样
        * context-param 标签内的配置文件，是 application 级别的， tomcat 会最先进行读取的。这时候 servlet 可能还没有开始启动
        * init-param 标签内的配置文件，是 servlet 级别的， tomcat 只有在创建具体的 servlet 时，才会读取并将其交给 servlet 
    * web.xml里面可以定义两种参数：
        * application范围内的参数，存放在servletcontext中，在web.xml中配置如下：
        ```xml
        <context-param>
            <param-name>context/param</param-name>
            <param-value>avalible during application</param-value>
        </context-param>
        ```
        * servlet范围内的参数，只能在servlet的init()方法中取得，在web.xml中配置如下：
        ```xml
        <servlet>
            <servlet-name>MainServlet</servlet-name>
            <servlet-class>com.wes.controller.MainServlet</servlet-class>
            <init-param>
                <param-name>param1</param-name>
                <param-value>avalible in servlet init()</param-value>
            </init-param>
            <load-on-startup>0</load-on-startup>
        </servlet>
        ```
    * 取用方法
    ```java
    package com.wes.controller;
    import javax.servlet.ServletException;
    import javax.servlet.http.HttpServlet;
    public class MainServlet extends HttpServlet ...{
        public MainServlet() ...{
            super();
        }
        public void init() throws ServletException ...{
            // 下面的两个参数param1是在servlet中存放的"
            System.out.println(this.getInitParameter("param1"));
            // 下面的参数是存放在servletcontext中的
            System.out.println(getServletContext().getInitParameter("context/param"));
        }
    }
    ```










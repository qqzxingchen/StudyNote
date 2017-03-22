
* 需求：访问url <http://localhost:8080/hello.mvc> ，返回一个页面

### 试一试-Hello World Spring MVC 应用程序

* 创建Maven项目
```bash
mvn archetype:generate -DarchetypeArtifactId=maven-archetype-webapp -DgroupId=com.wiley.beginningspring -DartifactId=basic -DarchetypeCatalog=internal
```

* 添加项目对 spring-webmvc 的依赖，以及 spring-webmvc 的依赖项： spring-core spring-beans spring-context spring-web
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-webmvc</artifactId>
        <version>4.0.5.RELEASE</version>
    </dependency>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-core</artifactId>
        <version>4.0.5.RELEASE</version>
    </dependency>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-beans</artifactId>
        <version>4.0.5.RELEASE</version>
    </dependency>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>4.0.5.RELEASE</version>
    </dependency>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-web</artifactId>
        <version>4.0.5.RELEASE</version>
    </dependency>
    <!-- Added for debugging purposes -->
    <dependency>
        <groupId>javax.servlet</groupId>
        <artifactId>javax.servlet-api</artifactId>
        <version>3.1.0</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

* web.xml （ /webapp/WEB-INF/web.xml ）中使用 URL 映射定义 Dispatcher Servlet
```xml
 <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
      version="3.1">
    <!-- 指定servlet信息 -->
    <servlet>
        <servlet-name>springmvc</servlet-name>
        <!-- 指定某 servlet 的入口地址为 org.springframework.web.servlet.DispatcherServlet -->
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <load-on-startup>1</load-on-startup>

        <!-- init-param 节点元素是为了指定一些额外的值 -->
        <init-param>
            <!-- 
                Servlet 在启动时，需要加载一个 xml 文件（就是之前定义bean的文件），以便获取 Spring 应用程序的上下文
                    Spring 应用程序的上下文，即 WebApplicationContext 的实现
                    WebApplicationContext接口，即一个继承自 ApplicationContext 接口的接口，提供以 Web 为中心的相关功能
                默认情况下，将会找 WEB-INF/${servlet-name}-servlet.xml 文件，对于本例来说，就是 WEB-INF/springmvc-servlet.xml 文件
                当然也可以手动指定该文件的路径，如下
            -->
            <param-name>contextConfigLocation</param-name>
            <!-- 这个路径也是 WEB-INF/springmvc-servlet.xml 文件 --> 
            <param-value>classpath:springmvc-servlet.xml</param-value>
        </init-param>
    </servlet>

    <!--
        一个tomcat只能有一个web.xml文件，但是有时候需要在一个tomcat中放多个servlet（web服务），
        因此就可以定义多个 servlet 节点元素，然后通过 url 的映射区分到底使用哪个servlet
    -->
    <servlet-mapping>
        <!-- url以 .mvc 结尾的请求将会分发到 springmvc 这个 servlet 中 -->
        <servlet-name>springmvc</servlet-name>
        <url-pattern>*.mvc</url-pattern>
    </servlet-mapping>
</web-app>
```


* springmvc-servlet.xml 文件
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans 
                              http://www.springframework.org/schema/beans/spring-beans-4.0.xsd 
                              http://www.springframework.org/schema/context
                              http://www.springframework.org/schema/context/spring-context-4.0.xsd">
    <context:component-scan base-package="com.wiley.beginningspring.ch3" />
    <context:annotation-config />
    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <!-- 
            这里将视图名与视图文件（.jsp）对应起来了 
        -->
        <property name="prefix" value="/WEB-INF/pages/" />
        <property name="suffix" value=".jsp" />
    </bean>
</beans>
```

* HelloReaderController.java 文件
```java
##### ${project_root}/src/main/java/com/wiley/beginningspring/ch3/controller/HelloReaderController.java
package com.wiley.beginningspring.ch3.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class HelloReaderController {
    @RequestMapping(value = "/hello")
    public ModelAndView sayHello() {
        ModelAndView mv = new ModelAndView();

        // 在 view 的上下文中，添加一个 k-v 
        mv.addObject("message", "Hello Reader!");

        // 这里指定 view 的名字为 helloReader 
        // 由于 springmvc-servlet.xml 中指定了视图名与视图文件的对照关系: ${prefix}${view-name}${suffix} （这里似乎大小写不敏感）
        // 即视图名 helloReader 将会与视图文件 /WEB-INF/pages/helloReader.jsp 文件对应
        mv.setViewName("helloReader");
        return mv;
    }
}
```

* helloReader.jsp
```html
<html>
<body>
    ${message}
</body>
</html>
```

* 部署
```bash
# 首先需要将项目打包成war包
$ mvn package

# 然后将 war 包移动到 tomcat 相应目录下
# basic.war 是生成的打包文件，可以查看pom.xml。该文件可以通过 unzip 解压
# 环境变量 CATALINA_HOME 是tomcat的根目录
$ mv target/basic.war ${CATALINA_HOME}/webapps/

# 启动 tomcat 
$ ${CATALINA_HOME}/bin/startup.sh

# 在浏览器中输入 http://localhost:8080/basic/hello.mvc ，即可看到效果
# 注意，在 tomcat 已启动的情况下，将 basic.war 拷贝到 webapps 目录下后，
#       tomcat将会新建一个与 .war 包同名的文件夹，并把 .war 包中的内容解压到该文件夹中，相当于是执行了下面的操作序列：
#       $ cd webapps ; mkdir basic ; unzip basic.war -d basic/

# url中的basic实际上是这个文件夹的名字。如果修改了这个名字，那么url中的basic部分将需要同步修改
# 通过执行下面的命令，可以发现 http://localhost:8080/basic_temp/hello.mvc 可以访问了
$ mv basic basic_temp               

# 而这时候，原来的地址（http://localhost:8080/basic/hello.mvc）还是可以访问的，因为tomcat会保证 basic.war 包与 basic 文件夹的同步
#       新建 basic.war 包，tomcat会自动新建 basic 目录，并将 basic.war 中的内容解压到 basic 目录下
#       删除 basic.war 包，tomcat会自动删除 basic 目录
#       删除 basic 目录，tomcat也会自动创建 basic 目录，并解压 basic.war
```




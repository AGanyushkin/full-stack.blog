Title: Spring Boot and NestJS
Date: 2022-03-12 21:00
Category: Spring
Tags: nestjs, spring, spring boot, spring mvc
Author: Andrey G
Status: published
Summary: Spring Boot and NestJS comparision
Lang: en
---

For me it is interesting to compare Spring Boot and NestJS because they has similar core ideas based on Inversion of Control and Dependency Injection. Of course Spring Boot significantly more powerful, I understand it. Both frameworks provide ability for us to write short and expressive code. And it will be interesting to compare two implementations for one project.

NestJS development experience pretty similar to Angular experience and if we can use NestJS for simple backend services instead of Spring Boot – it means we can reduce complexity in development process for full stack developers.

I would like to use “fake api” project to do this comparision. “fake api” project will implements endpoints for account and message generation, and also simple method to generate account online/offline status.

As usual, all code can be founded here:

[https://github.com/AGanyushkin/demo-fakeapi-springboot](https://github.com/AGanyushkin/demo-fakeapi-springboot)

[https://github.com/AGanyushkin/demo-fakeapi-nestjs](https://github.com/AGanyushkin/demo-fakeapi-nestjs)

# Domain entities

##### typescript
```typescript
export interface Account {
  id: string
  fullName: string
  email: string
  active: boolean
}

export interface Message {
  id: string
  ownerId: string
  text: string
}

export enum OnlineStatusEnum {
  ONLINE = 'ONLINE',
  OFFLINE = 'OFFLINE'
}

export interface OnlineStatus {
  accountId: string
  status: OnlineStatusEnum
}
```

##### java
```java
@AllArgsConstructor
@Getter
@Builder
public class Account {
    private String id;
    private String fullName;
    private String email;
    private boolean active;
}

@AllArgsConstructor
@Getter
@Builder
public class Message {
    private String id;
    private String ownerId;
    private String text;
}

@AllArgsConstructor
@Getter
@Builder
public class OnlineStatus {
    private String accountId;
    private OnlineStatusEnum status;

    public enum OnlineStatusEnum {
        ONLINE,
        OFFLINE
    }
}
```

# Controllers

For simple api implementations it is very important to have simpliest way to describe api endpoints. In Spring Boot this is done very simply

##### java
```java
@RequiredArgsConstructor
@RestController
@RequestMapping(path = "/message")
public class MessageController {
    private final MessageGeneratorService messageGeneratorService;


    @GetMapping(produces = APPLICATION_JSON_VALUE)
    @ResponseStatus(HttpStatus.OK)
    @ResponseBody
    public List<Message> generateAccounts(@RequestParam String ownerId, @RequestParam int size) {
        return messageGeneratorService.generateMessages(ownerId, size);
    }
}
```

We can inject service `MessageGeneratorService` and describe api endpoint.

In NestJS it can be done similarly

##### typescript
```typescript
@Controller('/message')
export class MessageController {
  constructor(private messageGeneratorService: MessageGeneratorService) {
  }

  @Get()
  @HttpCode(200)
  @Header('Content-Type', 'application/json')
  @Header('Access-Control-Allow-Origin', '*')
  generateMessages(@Query("ownerId") ownerId: string,
                   @Query("size") size: number): Observable<Message[]> {
    return this.messageGeneratorService.generateMessages(ownerId, +size)
  }
}
```

really similar, right?

# Services

Now a couple of words about service. And here the similar situation, both implementation looks the same

##### typescript
```typescript
@Injectable()
export class MessageGeneratorService {
  generateMessages(ownerId: string, numberOfMessages: number):
 Observable<Message[]> {
    return range(1, numberOfMessages)
      .pipe(
        switchMap((i: number): Observable<Message> => of({
          id: faker.datatype.uuid(),
          ownerId,
          text: faker.lorem.paragraph()
        })),
        toArray<Message>()
      )
  }
}
```

##### java
```java
@Service
public class MessageGeneratorService {
    public List<Message> generateMessages(String ownerId, int numberOfMessages) {
        var faker = new Faker();
        return IntStream.range(0, numberOfMessages)
                .mapToObj(i -> Message.builder()
                        .id(UUID.randomUUID().toString())
                        .ownerId(ownerId)
                        .text(faker.yoda().quote())
                        .build())
                .toList();
    }
}
```

It’s really similary implementations

# CORS

Cross-Origin Resource Sharing. CORS configuration in both frameworks can be provided as described below

##### java
```java
// In Spring Boot CORS can be configured with annotation on dedicated api method
@CrossOrigin
@GetMapping(produces = APPLICATION_JSON_VALUE)
@ResponseStatus(HttpStatus.OK)
@ResponseBody
public OnlineStatus getAccountOnlineStatus(@RequestParam String accountId) {
...

// or with global configuration
@Configuration
@EnableWebMvc
public class MvcConfiguration implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**");
    }
}
```

##### typescript
```typescript
// In NestJS CORS can be configured with decorator
// @Header('Access-Control-Allow-Origin', '*')
// also, here we can add other cors options with headers
@Get()
@HttpCode(200)
@Header('Content-Type', 'application/json')
@Header('Access-Control-Allow-Origin', '*')
getAccountStatus(@Query("accountId") accountId: string): OnlineStatus {
...
```

# Conclusion

I was surprised by NestJS. This framework very similar to both Spring Boot and Angular frameworks. NestJS provides and/or implements significantly less abilities, integrations, approaches than Spring Boot, but his abilities enough to support common SPA applications. NestJS it is Angular in backend and it’s very easy to switch between Angular and NestJS components.

Interesting note here, monorepo which can based on [https://nx.dev/](https://nx.dev/) provides for us the simple way to shared code between Angular and NestJS.


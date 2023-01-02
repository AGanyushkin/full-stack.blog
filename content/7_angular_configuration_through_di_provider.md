Title: Angular configuration through DI Provider
Date: 2022-02-12 21:00
Category: Angular
Tags: angular, di provider
Author: Andrey G
Status: published
Summary: DI Provider in Angular
Lang: en
---

In Angular framework we can specify “something” which called token and it is possible to use this thing in DI Provider. This ability can be used to configure some shared code with different parameters.

sample implementation: [https://github.com/AGanyushkin/demo-angular-token-injection](https://github.com/AGanyushkin/demo-angular-token-injection)

some docs: [https://angular.io/api/core/InjectionToken](https://angular.io/api/core/InjectionToken)

# Sample

In demo application we have core domain type – account. And we have common implementation for service

##### account.service.ts
```typescript
@Injectable()
export class AccountService {
  constructor(@Inject(ACCOUNT_TYPE) private accountType: AccountTypeType) {
  }

  getListOfAccounts(): Observable<Account[]> {
    return of(DATA[this.accountType])
  }
}
```

This implementation so simple, but it can illustrate the main idea. We have service which can be configured with one parameter to provide more than one data types.

In code above we can see how service can be configured with injectable token

```typescript
constructor(@Inject(ACCOUNT_TYPE) private accountType: AccountTypeType) { }
```

and service DI provider will inject something which `AccountTypeType` into service constructor.

To specify token we need to put only one line of code

##### token definition
```typescript
type AccountTypeType = 'customer' | 'admin';
export const ACCOUNT_TYPE = new InjectionToken<AccountTypeType>('accountType');
```

Now we know how to define token and how to use it, the last one what we need to do – pass right token in right places.

# How to use for configuration

For example, we have two types: `'customer' | 'admin'` and two components to show these data lists.

It is pretty simple to configure token for different parts of our angular application. Let’s see how we can configure `AccountService` for these `customer` and admin types

# Inject in module level

##### admin.module.ts
```typescript
@NgModule({
  ...
  providers: [
    AccountService,
    { provide: ACCOUNT_TYPE, useValue: "admin" }
  ]
})
export class AdminModule { }
```

as result, token will be passed into `AccountService` inside `AdminModule` module.

# Inject in component level

It possible to configure token in component level. As result – you can have `AccountService` with different configuration individually for each component in one module.

##### customer-list-view.component.ts
```typescript
@Component({
  ...
  providers: [
    { provide: ACCOUNT_TYPE, useValue: 'customer' },
    AccountService
  ]
})
export class CustomerListViewComponent implements OnInit {
...
```

# Conclusion

I have no much to say here. It can be used in some cases i think.


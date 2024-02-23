import asyncio
from fastapi import APIRouter, status
from fastapi.requests import Request
from main import template_engine


router = APIRouter()


@router.get('/account', status_code=status.HTTP_200_OK)
async def get_account(request: Request):
    vm = AccountViewModel(request)
    await vm.load()
    return template_engine.TemplateResponse('account/index.html', {"request": request, "vm": vm.to_dict()})


@router.get('/account/register', status_code=status.HTTP_200_OK)
def register_get(request: Request):
    vm = RegisterViewModel(request)
    return template_engine.TemplateResponse('account/register.html', {"request": request, "vm": vm.to_dict()})


@router.post('/account/register')
@template(template_file='account/register.pt')
async def register_post(request: Request):
    vm = RegisterViewModel(request)
    await vm.load()
    if vm.error:
        return vm.to_dict()
    # Create account
    account = await account_service.create_account(vm.name, vm.email, vm.password)
    # Login user
    response = RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, account.id)

    return response


@router.get('/account/login')
@template(template_file='account/login.pt')
def login_get(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.post('/account/login')
@template(template_file='account/login.pt')
async def login_post(request: Request):
    vm = LoginViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    user = await account_service.login_account(vm.email, vm.password)
    if not user:
        await asyncio.sleep(3)
        vm.error = 'The account does not exist or the password is wrong'
        return vm.to_dict()

    response = RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, user.id)

    return response


@router.get('/account/logout')
def logout():
    response = RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)
    return response
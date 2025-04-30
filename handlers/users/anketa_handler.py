from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.check import check_up
from loader import dp, bot
from states.anketa import Data
@dp.callback_query_handler(text="ik")
async def sotuvchi_handler(callback:types.CallbackQuery):
    await callback.message.answer("Ijaraga kvartira berish uchun ariza topshirish.\n"
                                  "Hozir sizga birnechta savol beriladi!\n"
                                  "Har biriga javob bering!\n"
                                  "Agar oxirida hammasi to'g'ri bo'lsa 'HA' deb yozing\n"
                                  "--arizangiz Adminga yuboriladi")
    await callback.message.answer("Ismingizni kiriting")
    await Data.name.set()
@dp.message_handler(state=Data.name)
async def get_name(message:types.Message,state:FSMContext):
    name=message.text
    await state.update_data(
        {"name":name}
    )
    await message.answer("Kvartira manzilini kiriting")
    await Data.adress.set()
@dp.message_handler(state=Data.adress)
async def get_adress(message: types.Message, state: FSMContext):
    adress = message.text
    await state.update_data(
        {"adress": adress}
    )

    await message.answer("Nechinchi qavatda joylashgan?")
    await Data.floor.set()
@dp.message_handler(state=Data.floor)
async def get_floor(message:types.Message,state:FSMContext):
    floor=message.text
    await state.update_data(
        {"floor":floor}
    )
    await message.answer("Xonalar soni nechta")
    await Data.rooms.set()
@dp.message_handler(state=Data.rooms)
async def get_rooms(message:types.Message,state:FSMContext):
    rooms=message.text
    await state.update_data(
        {"rooms":rooms}
    )
    await message.answer("Uy maydoni qancha (m^2)")
    await Data.area.set()
@dp.message_handler(state=Data.area)
async def get_area(message:types.Message,state:FSMContext):
    area=message.text
    await state.update_data(
        {"area":area}
    )
    await message.answer("Narxi qancha?")
    await Data.price.set()
@dp.message_handler(state=Data.price)
async def get_price(message:types.Message,state:FSMContext):
    price=message.text
    await state.update_data(
        {"price":price}
    )
    await message.answer("Siz bilan bog'lanish uchun tel-raqam yoki (@telegram.akk) qoldiring")
    await Data.contact.set()
@dp.message_handler(state=Data.contact)
async def get_contact(message:types.Message,state:FSMContext):
    contact=message.text
    await state.update_data(
        {"contact":contact}
    )

# Ma'lumotlarni qayta oqiymiz
    data = await state.get_data()
    name=data.get("name")
    adress=data.get("adress")
    floor=data.get("floor")
    rooms=data.get("rooms")
    area=data.get("area")
    price=data.get("price")
    contact=data.get("contact")
    result=f"QUYIDAGI MA'LUMOTLAR OLINDI👇\n"
    result+=(
        f"E'lon beruvchi: {name}\n"
        f"📍Manzil: {adress}\n"
        f"🌃Qavat: {floor} qavat\n"
        f"🏠Xona: {rooms} xona\n"
        f"🗺Uy maydoni: {area}m^2\n"
        f"💲Narxi: {price}$\n"
        f"📞Murojat uchun: {contact}"
    )
    await bot.send_message(ADMINS[0], result)

@dp.callback_query_handler(text="iy")
async def sotuvchi_handler(callback:types.CallbackQuery):
    await callback.message.answer("Ijaraga yotoqxona berish uchun ariza topshirish.\n"
                                  "Hozir sizga birnechta savol beriladi!\n"
                                  "Har biriga javob bering!\n"
                                  "Agar oxirida hammasi to'g'ri bo'lsa 'HA' deb yozing\n"
                                  "--arizangiz Adminga yuboriladi")
    await callback.message.answer("Ismingizni kiriting")
    await Data.name.set()
@dp.message_handler(state=Data.name)
async def get_name(message:types.Message,state:FSMContext):
    name=message.text
    await state.update_data(
        {"name":name}
    )
    await message.answer("Kvartira manzilini kiriting")
    await Data.adress.set()
@dp.message_handler(state=Data.adress)
async def get_adress(message: types.Message, state: FSMContext):
    adress = message.text
    await state.update_data(
        {"adress": adress}
    )

    await message.answer("Nechinchi qavatda joylashgan?")
    await Data.floor.set()
@dp.message_handler(state=Data.floor)
async def get_floor(message:types.Message,state:FSMContext):
    floor=message.text
    await state.update_data(
        {"floor":floor}
    )
    await message.answer("Xonalar soni nechta")
    await Data.rooms.set()
@dp.message_handler(state=Data.rooms)
async def get_rooms(message:types.Message,state:FSMContext):
    rooms=message.text
    await state.update_data(
        {"rooms":rooms}
    )
    await message.answer("Uy maydoni qancha (m^2)")
    await Data.area.set()
@dp.message_handler(state=Data.area)
async def get_area(message:types.Message,state:FSMContext):
    area=message.text
    await state.update_data(
        {"area":area}
    )
    await message.answer("Narxi qancha?")
    await Data.price.set()
@dp.message_handler(state=Data.price)
async def get_price(message:types.Message,state:FSMContext):
    price=message.text
    await state.update_data(
        {"price":price}
    )
    await message.answer("Siz bilan bog'lanish uchun tel-raqam yoki (@telegram.akk) qoldiring")
    await Data.contact.set()
@dp.message_handler(state=Data.contact)
async def get_contact(message:types.Message,state:FSMContext):
    contact=message.text
    await state.update_data(
        {"contact":contact}
    )

# Ma'lumotlarni qayta oqiymiz
    data = await state.get_data()
    name=data.get("name")
    adress=data.get("adress")
    floor=data.get("floor")
    rooms=data.get("rooms")
    area=data.get("area")
    price=data.get("price")
    contact=data.get("contact")
    result=f"QUYIDAGI MA'LUMOTLAR OLINDI👇\n"
    result+=(
        f"E'lon beruvchi: {name}\n"
        f"📍Manzil: {adress}\n"
        f"🌃Qavat: {floor} qavat\n"
        f"🏠Xona: {rooms} xona\n"
        f"🗺Uy maydoni: {area}m^2\n"
        f"💲Narxi: {price}$\n"
        f"📞Murojat uchun: {contact}"
    )
    await bot.send_message(ADMINS[0], result)
@dp.callback_query_handler(text="ts")
async def sotuvchi_handler(callback:types.CallbackQuery):
    await callback.message.answer("Ijaraga kvartira berish uchun ariza topshirish.\n"
                                  "Hozir sizga birnechta savol beriladi!\n"
                                  "Har biriga javob bering!\n"
                                  "Agar oxirida hammasi to'g'ri bo'lsa 'HA' deb yozing\n"
                                  "--arizangiz Adminga yuboriladi")
    await callback.message.answer("Ismingizni kiriting")
    await Data.name.set()
@dp.message_handler(state=Data.name)
async def get_name(message:types.Message,state:FSMContext):
    name=message.text
    await state.update_data(
        {"name":name}
    )
    await message.answer("Kvartira manzilini kiriting")
    await Data.adress.set()
@dp.message_handler(state=Data.adress)
async def get_adress(message: types.Message, state: FSMContext):
    adress = message.text
    await state.update_data(
        {"adress": adress}
    )

    await message.answer("Nechinchi qavatda joylashgan?")
    await Data.floor.set()
@dp.message_handler(state=Data.floor)
async def get_floor(message:types.Message,state:FSMContext):
    floor=message.text
    await state.update_data(
        {"floor":floor}
    )
    await message.answer("Xonalar soni nechta")
    await Data.rooms.set()
@dp.message_handler(state=Data.rooms)
async def get_rooms(message:types.Message,state:FSMContext):
    rooms=message.text
    await state.update_data(
        {"rooms":rooms}
    )
    await message.answer("Uy maydoni qancha (m^2)")
    await Data.area.set()
@dp.message_handler(state=Data.area)
async def get_area(message:types.Message,state:FSMContext):
    area=message.text
    await state.update_data(
        {"area":area}
    )
    await message.answer("Narxi qancha?")
    await Data.price.set()
@dp.message_handler(state=Data.price)
async def get_price(message:types.Message,state:FSMContext):
    price=message.text
    await state.update_data(
        {"price":price}
    )
    await message.answer("Siz bilan bog'lanish uchun tel-raqam yoki (@telegram.akk) qoldiring")
    await Data.contact.set()
@dp.message_handler(state=Data.contact)
async def get_contact(message:types.Message,state:FSMContext):
    contact=message.text
    await state.update_data(
        {"contact":contact}
    )

# Ma'lumotlarni qayta oqiymiz
    data = await state.get_data()
    name=data.get("name")
    adress=data.get("adress")
    floor=data.get("floor")
    rooms=data.get("rooms")
    area=data.get("area")
    price=data.get("price")
    contact=data.get("contact")
    result=f"QUYIDAGI MA'LUMOTLAR OLINDI👇\n"
    result+=(
        f"E'lon beruvchi: {name}\n"
        f"📍Manzil: {adress}\n"
        f"🌃Qavat: {floor} qavat\n"
        f"🏠Xona: {rooms} xona\n"
        f"🗺Uy maydoni: {area}m^2\n"
        f"💲Narxi: {price}$\n"
        f"📞Murojat uchun: {contact}"
    )
    await message.answer("Malumotlar to'g'rimi?")

    await bot.send_message(ADMINS[0], result)
    await state.finish()



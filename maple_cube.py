import numpy as np

wapon_result = []
emblem_result = []
sub_wapon_result = []
force_and_soul_result = []
shield_result = []
cap_result = []
top_result = []
suit_result = []
bottom_result = []
shoes_result = []
gloves_result = []
cloak_result = []
belt_result = []
shoulder_result = []
face_result = []
eyes_result = []
earring_result = []
ring_result = []
necklace_result = []
heart_result = []

class redcube:

    #무기_레드 
    wapon_1 = [
        'STR:+12%','DEX:+12%','INT:+12%','LUK:+12%',
        '공격력:+12%','마력+12%','크확:+12%','데미지:+12%','올스탯:+9%',
        '렙당 공격력:+1','렙당 마력:+1',
        '방무:+35%','방무:+40%',
        '보공:+30%','보공:+35%','보공:+40%'
        ]
    wapon_2 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '공격력 : +9%','마력 : +9%','크확 : +9%','데미지 : +9%','올스탯 : +6%',
        '방무 : +30%','보공 : +30%',
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%','크확 : +12%','데미지 : +12%','올스탯 : +9%',
        '렙당 공격력 : +1','렙당 마력 : +1',
        '방무 : +35%','방무 : +40%',
        '보공 : +30%','보공 : +35%','보공 : +40%'
        ]
    wapon_3 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '공격력 : +9%','마력 : +9%','크확 : +9%','데미지 : +9%','올스탯 : +6%',
        '방무 : +30%','보공 : +30%',
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%','크확 : +12%','데미지 : +12%','올스탯 : +9%',
        '렙당 공격력 : +1','렙당 마력 : +1',
        '방무 : +35%','방무 : +40%',
        '보공 : +30%','보공 : +35%','보공 : +40%'
        ]
    #엠블렘_레드 
    emblem_1 = [
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%','크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%'
        ]
    emblem_2 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '공격력 : +9%','마력 : +9%','크리티컬 확률 : +9%','데미지 : +9%','올스탯 : +6%',
        '몬스터 방어율 무시 : +30%',
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%','크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%'
        ]
    emblem_3 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '공격력 : +9%','마력 : +9%','크리티컬 확률 : +9%','데미지 : +9%','올스탯 : +6%',
        '몬스터 방어율 무시 : +30%',
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%','크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%'
        ]
    #보조무기_레드 
    sub_wapon_1 = [
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%','크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%','보스 몬스터 공격 시 데미지 : +35%','보스 몬스터 공격 시 데미지 : +40%'
        ]
    sub_wapon_2 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '공격력 : +9%','마력 : +9%','크리티컬 확률 : +9%','데미지 : +9%','올스탯 : +6%',
        '몬스터 방어율 무시 : +30%',
        '피격 시 5% 확률로 데미지의 20% 무시','피격 시 5% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%',
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%','크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%','보스 몬스터 공격 시 데미지 : +35%','보스 몬스터 공격 시 데미지 : +40%'
        ]
    sub_wapon_3 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '공격력 : +9%','마력 : +9%','크리티컬 확률 : +9%','데미지 : +9%','올스탯 : +6%',
        '몬스터 방어율 무시 : +30%',
        '피격 시 5% 확률로 데미지의 20% 무시','피격 시 5% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%',
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%','크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%','보스 몬스터 공격 시 데미지 : +35%','보스 몬스터 공격 시 데미지 : +40%'
        ]
    #포스실드_소울링_레드 
    force_and_soul_1 = [
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%','크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%','보스 몬스터 공격 시 데미지 : +35%','보스 몬스터 공격 시 데미지 : +40%'
        ]
    force_and_soul_2 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '공격력 : +9%','마력 : +9%','크리티컬 확률 : +9%','데미지 : +9%','올스탯 : +6%',
        '몬스터 방어율 무시 : +30%',
        '피격 시 5% 확률로 데미지의 20% 무시','피격 시 5% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%',
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%','크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%','보스 몬스터 공격 시 데미지 : +35%','보스 몬스터 공격 시 데미지 : +40%'
        ]
    force_and_soul_3 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '공격력 : +9%','마력 : +9%','크리티컬 확률 : +9%','데미지 : +9%','올스탯 : +6%',
        '몬스터 방어율 무시 : +30%',
        '피격 시 5% 확률로 데미지의 20% 무시','피격 시 5% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%',
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%','크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%','보스 몬스터 공격 시 데미지 : +35%','보스 몬스터 공격 시 데미지 : +40%'
        ]
    #방패_레드 
    shield_1 = [
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%','크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%','보스 몬스터 공격 시 데미지 : +35%','보스 몬스터 공격 시 데미지 : +40%'
        ]
    shield_2 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '공격력 : +9%','마력 : +9%','크리티컬 확률 : +9%','데미지 : +9%','올스탯 : +6%',
        '몬스터 방어율 무시 : +30%',
        '피격 시 5% 확률로 데미지의 20% 무시','피격 시 5% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%',
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%','크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%','보스 몬스터 공격 시 데미지 : +35%','보스 몬스터 공격 시 데미지 : +40%'
        ]
    shield_3 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '공격력 : +9%','마력 : +9%','크리티컬 확률 : +9%','데미지 : +9%','올스탯 : +6%',
        '몬스터 방어율 무시 : +30%',
        '피격 시 5% 확률로 데미지의 20% 무시','피격 시 5% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%',
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%','크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '보스 몬스터 공격 시 데미지 : +30%','보스 몬스터 공격 시 데미지 : +35%','보스 몬스터 공격 시 데미지 : +40%'
        ]
    #모자_레드 
    cap_1 = [
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '최대 HP : +12%','최대 MP : +12%','방어력 : +12%','올스탯 : +9%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '모든 스킬의 재사용 대기시간 : -1초(10초 이하는 5%감소 5초 미만으로 감소 불가)','모든 스킬의 재사용 대기시간 : -2초(10초 이하는 10%감소 5초 미만으로 감소 불가)',
        '<쓸만한 어드밴스드 블레스> 스킬 사용 가능'
        ]
    cap_2 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '최대 HP : +9%','최대 MP : +9%','방어력 : +9%','올스탯 : +6%',
        '피격 시 5% 확률로 데미지의 20% 무시','피격 시 5% 확률로 데미지의 40% 무시','HP 회복 아이템 및 회복 스킬 효율 : +30%',
        '<쓸만한 미스틱 도어> 스킬 사용 가능',

        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '최대 HP : +12%','최대 MP : +12%','방어력 : +12%','올스탯 : +9%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '모든 스킬의 재사용 대기시간 : -1초(10초 이하는 5%감소 5초 미만으로 감소 불가)','모든 스킬의 재사용 대기시간 : -2초(10초 이하는 10%감소 5초 미만으로 감소 불가)',
        '<쓸만한 어드밴스드 블레스> 스킬 사용 가능'
        ]
    cap_3 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '최대 HP : +9%','최대 MP : +9%','방어력 : +9%','올스탯 : +6%',
        '피격 시 5% 확률로 데미지의 20% 무시','피격 시 5% 확률로 데미지의 40% 무시','HP 회복 아이템 및 회복 스킬 효율 : +30%',
        '<쓸만한 미스틱 도어> 스킬 사용 가능',

        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '최대 HP : +12%','최대 MP : +12%','방어력 : +12%','올스탯 : +9%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '모든 스킬의 재사용 대기시간 : -1초(10초 이하는 5%감소 5초 미만으로 감소 불가)','모든 스킬의 재사용 대기시간 : -2초(10초 이하는 10%감소 5초 미만으로 감소 불가)',
        '<쓸만한 어드밴스드 블레스> 스킬 사용 가능'
        ]
    #상의_레드 
    top_1 = [
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '최대 HP : +12%','최대 MP : +12%','방어력 : +12%','올스탯 : +9%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '피격 후 무적시간 : +3초','피격 시 4% 확률로 7초간 무적'
    ]
    top_2 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '최대 HP : +9%','최대 MP : +9%','방어력 : +9%','올스탯 : +6%',
        '피격 시 5% 확률로 데미지의 20% 무시','피격 시 5% 확률로 데미지의 40% 무시',
        '피격 후 무적시간 : +2초','피격 시 2% 확률로 7초간 무적','30% 확률로 받은 피해의 50%를 반사',
        '30% 확률로 받은 피해의 70%를 반사','HP 회복 아이템 및 회복 스킬 효율 : +30%',

        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '최대 HP : +12%','최대 MP : +12%','방어력 : +12%','올스탯 : +9%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '피격 후 무적시간 : +3초','피격 시 4% 확률로 7초간 무적'
    ]
    top_3 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '최대 HP : +9%','최대 MP : +9%','방어력 : +9%','올스탯 : +6%',
        '피격 시 5% 확률로 데미지의 20% 무시','피격 시 5% 확률로 데미지의 40% 무시',
        '피격 후 무적시간 : +2초','피격 시 2% 확률로 7초간 무적','30% 확률로 받은 피해의 50%를 반사',
        '30% 확률로 받은 피해의 70%를 반사','HP 회복 아이템 및 회복 스킬 효율 : +30%',

        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '최대 HP : +12%','최대 MP : +12%','방어력 : +12%','올스탯 : +9%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '피격 후 무적시간 : +3초','피격 시 4% 확률로 7초간 무적'
    ]
    #한벌옷_레드 
    suit_1 = [
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '최대 HP : +12%','최대 MP : +12%','방어력 : +12%','올스탯 : +9%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '피격 후 무적시간 : +3초','피격 시 4% 확률로 7초간 무적'
    ]
    suit_2 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '최대 HP : +9%','최대 MP : +9%','방어력 : +9%','올스탯 : +6%',
        '피격 시 5% 확률로 데미지의 20% 무시','피격 시 5% 확률로 데미지의 40% 무시',
        '피격 후 무적시간 : +2초','피격 시 2% 확률로 7초간 무적','30% 확률로 받은 피해의 50%를 반사',
        '30% 확률로 받은 피해의 70%를 반사','HP 회복 아이템 및 회복 스킬 효율 : +30%',

        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '최대 HP : +12%','최대 MP : +12%','방어력 : +12%','올스탯 : +9%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '피격 후 무적시간 : +3초','피격 시 4% 확률로 7초간 무적'
    ]
    suit_3 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '최대 HP : +9%','최대 MP : +9%','방어력 : +9%','올스탯 : +6%',
        '피격 시 5% 확률로 데미지의 20% 무시','피격 시 5% 확률로 데미지의 40% 무시',
        '피격 후 무적시간 : +2초','피격 시 2% 확률로 7초간 무적','30% 확률로 받은 피해의 50%를 반사',
        '30% 확률로 받은 피해의 70%를 반사','HP 회복 아이템 및 회복 스킬 효율 : +30%',

        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '최대 HP : +12%','최대 MP : +12%','방어력 : +12%','올스탯 : +9%',
        '피격 시 10% 확률로 데미지의 20% 무시','피격 시 10% 확률로 데미지의 40% 무시',
        '피격 후 무적시간 : +3초','피격 시 4% 확률로 7초간 무적'
    ]
    #하의_레드 
    bottom_1 = []
    bottom_2 = []
    bottom_3 = []
    #신발_레드 
    shoes_1 = []
    shoes_2 = []
    shoes_3 = []
    #장갑_레드 
    gloves_1 = []
    gloves_2 = []
    gloves_3 = []
    #망토_레드 
    cloak_1 = []
    cloak_2 = []
    cloak_3 = []
    #벨트_레드 
    belt_1 = []
    belt_2 = []
    belt_3 = []
    #어깨_레드 
    shoulder_1 = []
    shoulder_2 = []
    shoulder_3 = []
    #얼굴장식_레드 
    face_1 = []
    face_2 = []
    face_3 = []
    #눈장식_레드 
    eyes_1 = []
    eyes_2 = []
    eyes_3 = []
    #귀고리_레드 
    earring_1 = []
    earring_2 = []
    earring_3 = []
    #반지_레드 
    ring_1 = []
    ring_2 = []
    ring_3 = []
    #목걸이_레드 
    necklace_1 = []
    necklace_2 = []
    necklace_3 = []
    #기계심장_레드 
    heart_1 = []
    heart_2 = []
    heart_3 = []

    def wapon (a, b):
        if a == b:
            return
        else: 
            wapon_op_1 = np.random.choice(redcube.wapon_1, 1, p = 
            [0.097562,0.097562,0.097562,0.097562,0.048780,0.048780,0.048780,0.048780,0.073172,0.048780,0.048780,0.048780,0.048780,0.048780,0.048780,0.048780])
            wapon_op_2 = np.random.choice(redcube.wapon_2, 1, p = 
            [0.104651,0.104651,0.104651,0.104651,0.062791,0.062791,0.083721,0.062791,0.083721,0.062791,0.062791,
            0.009756,0.009756,0.009756,0.009756,0.004878,0.004878,0.004878,0.004878,0.007317,0.004878,0.004878,0.004878,0.004878,0.004878,0.004878,0.004878])
            wapon_op_3 = np.random.choice(redcube.wapon_3, 1, p = 
            [0.115116,0.115116,0.115116,0.115116,0.069070,0.069070,0.092093,0.069070,0.092093,0.069070,0.069070,
            0.000975,0.000975,0.000975,0.000975,0.000488,0.000488,0.000488,0.000488,0.000732,0.000488,0.000488,0.000488,0.000488,0.000488,0.000488,0.000488])
            
            wapon_result.append(str(wapon_op_1) + ' ' + str(wapon_op_2) + ' ' + str(wapon_op_3))
        redcube.wapon (a+1, b) 

    def emblem (a, b):
        if a == b:
            return
        else: 
            emblem_op_1 = np.random.choice(redcube.emblem_1, 1, p = 
            [0.114286,0.114286,0.114286,0.114286,0.057143,0.057143,0.057143,0.057143,0.085714,0.057143,0.057143,0.057142,0.057142])
            emblem_op_2 = np.random.choice(redcube.emblem_2, 1, p = 
            [0.112500,0.112500,0.112500,0.112500,0.067500,0.067500,0.090000,0.067500,0.090000,0.067501,
            0.011429,0.011429,0.011429,0.011429,0.005714,0.005714,0.005714,0.005714,0.008571,0.005714,0.005714,0.005714,0.005714])
            emblem_op_3 = np.random.choice(redcube.emblem_3, 1, p = 
            [0.123750,0.123750,0.123750,0.123750,0.074250,0.074250,0.099001,0.074251,0.099001,0.074250,
            0.001143,0.001143,0.001143,0.001143,0.000571,0.000571,0.000571,0.000571,0.000857,0.000571,0.000571,0.000571,0.000571])

            emblem_result.append(str(emblem_op_1) + ' ' + str(emblem_op_2) + ' ' + str(emblem_op_3))            
        redcube.emblem (a+1, b)

    def sub_wapon (a, b):
        if a == b:
            return
        else: 
            sub_wapon_op_1 = np.random.choice(redcube.sub_wapon_1, 1, p = 
            [0.085106,0.085106,0.085106,0.085106,0.042553,0.042553,0.042553,0.042553,0.063830,0.042553,0.042553,0.042553,0.042553,0.063830,0.063830,0.042554,0.042554,0.042554,])
            sub_wapon_op_2 = np.random.choice(redcube.sub_wapon_2, 1, p = 
            [0.088235,0.088235,0.088235,0.088235,0.052941,0.052941,0.070588,0.052941,0.070588,0.052941,0.070588,0.070588,0.052941,
            0.008511,0.008511,0.008511,0.008511,0.004255,0.004255,0.004255,0.004255,0.006383,0.004255,0.004255,0.004256,0.004256,0.006383,0.006383,0.004256,0.004256,0.004256
            ])
            sub_wapon_op_3 = np.random.choice(redcube.sub_wapon_3, 1, p = 
            [0.097059,0.097059,0.097059,0.097059,0.058235,0.058235,0.077646,0.058234,0.077646,0.058235,0.077647,0.077647,0.058235,
            0.000851,0.000851,0.000851,0.000851,0.000426,0.000426,0.000426,0.000426,0.000638,0.000426,0.000426,0.000426,0.000426,0.000638,0.000638,0.000426,0.000426,0.000426
            ])

            sub_wapon_result.append(str(sub_wapon_op_1) + ' ' + str(sub_wapon_op_2) + ' ' + str(sub_wapon_op_3))    
        redcube.sub_wapon (a+1, b)

    def force_and_soul (a, b):
        if a == b:
            return
        else: 
            force_and_soul_op_1 = np.random.choice(redcube.force_and_soul_1, 1, p = 
            [0.085106,0.085106,0.085106,0.085106,0.042553,0.042553,0.042553,0.042553,0.063830,0.042553,0.042553,0.042553,0.042553,0.063830,0.063830,0.042554,0.042554,0.042554])
            force_and_soul_op_2 = np.random.choice(redcube.force_and_soul_2, 1, p = 
            [0.088235,0.088235,0.088235,0.088235,0.052941,0.052941,0.070588,0.052941,0.070588,0.052941,0.070588,0.070588,0.052941,
            0.008511,0.008511,0.008511,0.008511,0.004255,0.004255,0.004255,0.004255,0.006383,0.004255,0.004255,0.004256,0.004256,0.006383,0.006383,0.004256,0.004256,0.004256])
            force_and_soul_op_3 = np.random.choice(redcube.force_and_soul_3, 1, p = 
            [0.097059,0.097059,0.097059,0.097059,0.058235,0.058235,0.077647,0.058235,0.077647,0.058235,0.077647,0.077647,0.058235,
            0.000851,0.000851,0.000851,0.000851,0.000426,0.000426,0.000426,0.000426,0.000638,0.000426,0.000426,0.000426,0.000426,0.000638,0.000638,0.000425,0.000425,0.000425])

            force_and_soul_result.append(str(force_and_soul_op_1) + ' ' + str(force_and_soul_op_2) + ' ' + str(force_and_soul_op_3))    
        redcube.force_and_soul (a+1, b)
    force_and_soul_result 

    def shield (a, b):
        if a == b:
            return
        else: 
            shield_op_1 = np.random.choice(redcube.shield_1, 1, p = 
            [0.085106,0.085106,0.085106,0.085106,0.042553,0.042553,0.042553,0.042553,0.063830,0.042553,0.042553,0.042553,0.042553,0.063830,0.063830,0.042554,0.042554,0.042554])
            shield_op_2 = np.random.choice(redcube.shield_2, 1, p = 
            [0.088235,0.088235,0.088235,0.088235,0.052941,0.052941,0.070588,0.052941,0.070588,0.052941,0.070588,0.070588,0.052941,
            0.008511,0.008511,0.008511,0.008511,0.004255,0.004255,0.004255,0.004255,0.006383,0.004255,0.004255,0.004256,0.004256,0.006383,0.006383,0.004256,0.004256,0.004256])
            shield_op_3 = np.random.choice(redcube.shield_3, 1, p = 
            [0.097059,0.097059,0.097059,0.097059,0.058235,0.058235,0.077647,0.058235,0.077647,0.058235,0.077647,0.077647,0.058235,
            0.000851,0.000851,0.000851,0.000851,0.000426,0.000426,0.000426,0.000426,0.000638,0.000426,0.000426,0.000426,0.000426,0.000638,0.000638,0.000425,0.000425,0.000425])

            shield_result.append(str(shield_op_1) + ' ' + str(shield_op_2) + ' ' + str(shield_op_3))        
        redcube.shield (a+1, b)

    def cap (a, b):
        if a == b:
            return
        else: 
            cap_op_1 = np.random.choice(redcube.cap_1, 1, p = 
            [0.088889,0.088889,0.088889,0.088889,0.088889,0.088889,0.088889,0.066667,0.066666,0.066666,0.066667,0.044444,0.066667])
            cap_op_2 = np.random.choice(redcube.cap_2, 1, p = 
            [0.080357,0.080357,0.080357,0.080357,0.096429,0.096429,0.064286,0.064286,0.064286,0.064286,0.064286,0.064286,
            0.008888,0.008888,0.008888,0.008888,0.008889,0.008889,0.008889,0.006667,0.006667,0.006667,0.006667,0.004444,0.006667])
            cap_op_3 = np.random.choice(redcube.cap_3, 1, p = 
            [0.088393,0.088393,0.088393,0.088393,0.106071,0.106071,0.070714,0.070714,0.070714,0.070714,0.070714,0.070714,
            0.000889,0.000889,0.000889,0.000889,0.000889,0.000889,0.000889,0.000667,0.000667,0.000667,0.000667,0.000444,0.000667])
            
            cap_result.append(str(cap_op_1) + ' ' + str(cap_op_2) + ' ' + str(cap_op_3))
        redcube.cap (a+1, b)

    def top (a, b):
        if a == b:
            return
        else: 
            top_op_1 = np.random.choice(redcube.top_1, 1, p = 
            [0.093024,0.093024,0.093024,0.093024,0.093023,0.093023,0.093023,0.069767,0.069767,0.069767,0.069767,0.069767])
            top_op_2 = np.random.choice(redcube.top_2, 1, p = 
            [0.068183,0.068183,0.068183,0.068183,0.081818,0.081818,0.054545,0.054545,0.054545,0.054545,0.054545,0.054545,0.054545,0.027273,0.054545,
            0.009302,0.009302,0.009302,0.009302,0.009302,0.009302,0.009302,0.006977,0.006977,0.006977,0.006977,0.006977])
            top_op_3 = np.random.choice(redcube.top_3, 1, p = 
            [0.075000,0.075000,0.075000,0.075000,0.090000,0.090000,0.060000,0.060000,0.060000,0.060000,0.060000,0.060000,0.060000,0.030000,0.060000,
            0.000930,0.000930,0.000930,0.000930,0.000930,0.000930,0.000930,0.000698,0.000698,0.000698,0.000698,0.000698])
            
            top_result.append(str(top_op_1) + ' ' + str(top_op_2) + ' ' + str(top_op_3))
        redcube.top (a+1, b)

    def suit (a, b):
        if a == b:
            return
        else: 
            suit_op_1 = np.random.choice(redcube.suit_1, 1, p = 
            [0.093024,0.093024,0.093024,0.093024,0.093023,0.093023,0.093023,0.069767,0.069767,0.069767,0.069767,0.069767])
            suit_op_2 = np.random.choice(redcube.suit_2, 1, p =
            [0.068183,0.068183,0.068183,0.068183,0.081818,0.081818,0.054545,0.054545,0.054545,0.054545,0.054545,0.054545,0.054545,0.027273,0.054545,
            0.009302,0.009302,0.009302,0.009302,0.009302,0.009302,0.009302,0.006977,0.006977,0.006977,0.006977,0.006977])
            suit_op_3 = np.random.choice(redcube.suit_3, 1, p = 
            [0.075000,0.075000,0.075000,0.075000,0.090000,0.090000,0.060000,0.060000,0.060000,0.060000,0.060000,0.060000,0.060000,0.030000,0.060000,
            0.000930,0.000930,0.000930,0.000930,0.000930,0.000930,0.000930,0.000698,0.000698,0.000698,0.000698,0.000698])
            
            suit_result.append(str(suit_op_1) + ' ' + str(suit_op_2) + ' ' + str(suit_op_3))
        redcube.suit (a+1, b)

    def bottom (a, b):
        if a == b:
            return
        else: 
            bottom_op_1 = np.random.choice(redcube.bottom_1, 1, p = [])
            bottom_op_2 = np.random.choice(redcube.bottom_2, 1, p = [])
            bottom_op_3 = np.random.choice(redcube.bottom_3, 1, p = [])
            
            bottom_result.append(str() + ' ' + str() + ' ' + str())
        redcube.bottom (a+1, b)

    def shoes (a, b):
        if a == b:
            return
        else: 
            shoes_op_1 = np.random.choice(redcube.shoes_1, 1, p = [])
            shoes_op_2 = np.random.choice(redcube.shoes_2, 1, p = [])
            shoes_op_3 = np.random.choice(redcube.shoes_3, 1, p = [])
            
            shoes_result.append(str() + ' ' + str() + ' ' + str())
        redcube.shoes (a+1, b)

    def gloves (a, b):
        if a == b:
            return
        else: 
            gloves_op_1 = np.random.choice(redcube.gloves_1, 1, p = [])
            gloves_op_2 = np.random.choice(redcube.gloves_2, 1, p = [])
            gloves_op_3 = np.random.choice(redcube.gloves_3, 1, p = [])
            
            gloves_result.append(str() + ' ' + str() + ' ' + str())
        redcube.gloves (a+1, b)

    def cloak (a, b):
        if a == b:
            return
        else: 
            cloak_op_1 = np.random.choice(redcube.cloak_1, 1, p = [])
            cloak_op_2 = np.random.choice(redcube.cloak_2, 1, p = [])
            cloak_op_3 = np.random.choice(redcube.cloak_3, 1, p = [])
            
            cloak_result.append(str() + ' ' + str() + ' ' + str())
        redcube.cloak (a+1, b)

    def belt (a, b):
        if a == b:
            return
        else: 
            belt_op_1 = np.random.choice(redcube.belt_1, 1, p = [])
            belt_op_2 = np.random.choice(redcube.belt_2, 1, p = [])
            belt_op_3 = np.random.choice(redcube.belt_3, 1, p = [])
            
            belt_result.append(str() + ' ' + str() + ' ' + str())
        redcube.belt (a+1, b)

    def shoulder (a, b):
        if a == b:
            return
        else: 
            shoulder_op_1 = np.random.choice(redcube.shoulder_1, 1, p = [])
            shoulder_op_2 = np.random.choice(redcube.shoulder_2, 1, p = [])
            shoulder_op_3 = np.random.choice(redcube.shoulder_3, 1, p = [])
            
            shoulder_result.append(str() + ' ' + str() + ' ' + str())
        redcube.shoulder (a+1, b)

    def face (a, b):
        if a == b:
            return
        else: 
            face_op_1 = np.random.choice(redcube.face_1, 1, p = [])
            face_op_2 = np.random.choice(redcube.face_2, 1, p = [])
            face_op_3 = np.random.choice(redcube.face_3, 1, p = [])
            
            face_result.append(str() + ' ' + str() + ' ' + str())
        redcube.face (a+1, b)

    def eyes (a, b):
        if a == b:
            return
        else: 
            eyes_op_1 = np.random.choice(redcube.eyes_1, 1, p = [])
            eyes_op_2 = np.random.choice(redcube.eyes_2, 1, p = [])
            eyes_op_3 = np.random.choice(redcube.eyes_3, 1, p = [])
            
            eyes_result.append(str() + ' ' + str() + ' ' + str())
        redcube.eyes (a+1, b)
    def earring (a, b):
        if a == b:
            return
        else: 
            earring_op_1 = np.random.choice(redcube.earring_1, 1, p = [])
            earring_op_2 = np.random.choice(redcube.earring_2, 1, p = [])
            earring_op_3 = np.random.choice(redcube.earring_3, 1, p = [])
            
            earring_result.append(str() + ' ' + str() + ' ' + str())
        redcube.earring (a+1, b)

    def ring (a, b):
        if a == b:
            return
        else: 
            ring_op_1 = np.random.choice(redcube.ring_1, 1, p = [])
            ring_op_1 = np.random.choice(redcube.ring_2, 1, p = [])
            ring_op_1 = np.random.choice(redcube.ring_3, 1, p = [])
            
            ring_result.append(str() + ' ' + str() + ' ' + str())
        redcube.ring (a+1, b) 

    def necklace (a, b):
        if a == b:
            return
        else: 
            necklace_op_1 = np.random.choice(redcube.necklace_1, 1, p = [])
            necklace_op_2 = np.random.choice(redcube.necklace_2, 1, p = [])
            necklace_op_3 = np.random.choice(redcube.necklace_3, 1, p = [])
            
            necklace_result.append(str() + ' ' + str() + ' ' + str())
        redcube.necklace (a+1, b) 

    def heart (a, b):
        if a == b:
            return
        else: 
            heart_op_1 = np.random.choice(redcube.heart_1, 1, p = [])
            heart_op_2 = np.random.choice(redcube.heart_2, 1, p = [])
            heart_op_3 = np.random.choice(redcube.heart_3, 1, p = [])
            
            heart_result.append(str() + ' ' + str() + ' ' + str())
        redcube.heart (a+1, b) 

class blackcube:

    #무기_블랙 
    wapon_1 = []
    wapon_2 = []
    wapon_3 = []
    #엠블렘_블랙 
    emblem_1 = []
    emblem_2 = []
    emblem_3 = []
    #보조무기_블랙 
    sub_wapon_1 = []
    sub_wapon_2 = []
    sub_wapon_3 = []
    #포스실드_소울링_블랙 
    force_and_soul_1 = []
    force_and_soul_2 = []
    force_and_soul_3 = []
    #방패_블랙 
    shield_1 = []
    shield_2 = []
    shield_3 = []
    #모자_블랙 
    cap_1 = []
    cap_2 = []
    cap_3 = []
    #상의_블랙 
    top_1 = []
    top_2 = []
    top_3 = []
    #한벌옷_블랙 
    suit_1 = []
    suit_2 = []
    suit_3 = []
    #하의_블랙 
    bottom_1 = []
    bottom_2 = []
    bottom_3 = []
    #신발_블랙 
    shoes_1 = []
    shoes_2 = []
    shoes_3 = []
    #장갑_블랙 
    gloves_1 = []
    gloves_2 = []
    gloves_3 = []
    #망토_블랙 
    cloak_1 = []
    cloak_2 = []
    cloak_3 = []
    #벨트_블랙 
    belt_1 = []
    belt_2 = []
    belt_3 = []
    #어깨_블랙 
    shoulder_1 = []
    shoulder_2 = []
    shoulder_3 = []
    #얼굴장식_블랙 
    face_1 = []
    face_2 = []
    face_3 = []
    #눈장식_블랙 
    eyes_1 = []
    eyes_2 = []
    eyes_3 = []
    #귀고리_블랙 
    earring_1 = []
    earring_2 = []
    earring_3 = []
    #반지_블랙 
    ring_1 = []
    ring_2 = []
    ring_3 = []
    #목걸이_블랙 
    necklace_1 = []
    necklace_2 = []
    necklace_3 = []
    #기계심장_블랙 
    heart_1 = []
    heart_2 = []
    heart_3 = []

    def wapon (a, b):
        if a == b:
            return
        else: 
            wapon_op_1 = np.random.choice(blackcube.wapon_1, 1, p = 
            [])
            wapon_op_2 = np.random.choice(blackcube.wapon_2, 1, p = 
            [])
            wapon_op_3 = np.random.choice(blackcube.wapon_3, 1, p = 
            [])
            
            wapon_result.append(str(wapon_op_1) + ' ' + str(wapon_op_2) + ' ' + str(wapon_op_3))
        blackcube.wapon (a+1, b) 

    def emblem (a, b):
        if a == b:
            return
        else: 
            emblem_op_1 = np.random.choice(blackcube.emblem_1, 1, p = 
            [])
            emblem_op_2 = np.random.choice(blackcube.emblem_2, 1, p = 
            [])
            emblem_op_3 = np.random.choice(blackcube.emblem_3, 1, p = 
            [])

            emblem_result.append(str(emblem_op_1) + ' ' + str(emblem_op_2) + ' ' + str(emblem_op_3))            
        blackcube.emblem (a+1, b) 

    def sub_wapon (a, b):
        if a == b:
            return
        else: 
            sub_wapon_op_1 = np.random.choice(blackcube.sub_wapon_1, 1, p = [])
            sub_wapon_op_2 = np.random.choice(blackcube.sub_wapon_2, 1, p = [])
            sub_wapon_op_3 = np.random.choice(blackcube.sub_wapon_3, 1, p = [])

            sub_wapon_result.append(str(sub_wapon_op_1) + ' ' + str(sub_wapon_op_2) + ' ' + str(sub_wapon_op_3))    
        blackcube.sub_wapon (a+1, b) 

    def force_and_soul (a, b):
        if a == b:
            return
        else: 
            force_and_soul_op_1 = np.random.choice(blackcube.force_and_soul_1, 1, p = [])
            force_and_soul_op_2 = np.random.choice(blackcube.force_and_soul_2, 1, p = [])
            force_and_soul_op_3 = np.random.choice(blackcube.force_and_soul_3, 1, p = [])

            force_and_soul_result.append(str(force_and_soul_op_1) + ' ' + str(force_and_soul_op_2) + ' ' + str(force_and_soul_op_3))    
        blackcube.force_and_soul (a+1, b) 

    def shield (a, b):
        if a == b:
            return
        else: 
            shield_op_1 = np.random.choice(blackcube.shield_1, 1, p = [])
            shield_op_2 = np.random.choice(blackcube.shield_2, 1, p = [])
            shield_op_3 = np.random.choice(blackcube.shield_3, 1, p = [])

            shield_result.append(str(shield_op_1) + ' ' + str(shield_op_2) + ' ' + str(shield_op_3))        
        blackcube.shield (a+1, b) 

    def cap (a, b):
        if a == b:
            return
        else: 
            cap_op_1 = np.random.choice(blackcube.cap_1, 1, p = [])
            cap_op_2 = np.random.choice(blackcube.cap_2, 1, p = [])
            cap_op_3 = np.random.choice(blackcube.cap_3, 1, p = [])
            
            cap_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.cap (a+1, b) 

    def top (a, b):
        if a == b:
            return
        else: 
            top_op_1 = np.random.choice(blackcube.top_1, 1, p = [])
            top_op_2 = np.random.choice(blackcube.top_2, 1, p = [])
            top_op_3 = np.random.choice(blackcube.top_3, 1, p = [])
            
            top_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.top (a+1, b) 

    def suit (a, b):
        if a == b:
            return
        else: 
            suit_op_1 = np.random.choice(blackcube.suit_1, 1, p = [])
            suit_op_2 = np.random.choice(blackcube.suit_2, 1, p = [])
            suit_op_3 = np.random.choice(blackcube.suit_3, 1, p = [])
            
            suit_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.suit (a+1, b) 

    def bottom (a, b):
        if a == b:
            return
        else: 
            bottom_op_1 = np.random.choice(blackcube.bottom_1, 1, p = [])
            bottom_op_2 = np.random.choice(blackcube.bottom_2, 1, p = [])
            bottom_op_3 = np.random.choice(blackcube.bottom_3, 1, p = [])
            
            bottom_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.bottom (a+1, b) 

    def shoes (a, b):
        if a == b:
            return
        else: 
            shoes_op_1 = np.random.choice(blackcube.shoes_1, 1, p = [])
            shoes_op_2 = np.random.choice(blackcube.shoes_2, 1, p = [])
            shoes_op_3 = np.random.choice(blackcube.shoes_3, 1, p = [])
            
            shoes_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.shoes (a+1, b) 

    def gloves (a, b):
        if a == b:
            return
        else: 
            gloves_op_1 = np.random.choice(blackcube.gloves_1, 1, p = [])
            gloves_op_2 = np.random.choice(blackcube.gloves_2, 1, p = [])
            gloves_op_3 = np.random.choice(blackcube.gloves_3, 1, p = [])
            
            gloves_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.gloves (a+1, b) 

    def cloak (a, b):
        if a == b:
            return
        else: 
            cloak_op_1 = np.random.choice(blackcube.cloak_1, 1, p = [])
            cloak_op_2 = np.random.choice(blackcube.cloak_2, 1, p = [])
            cloak_op_3 = np.random.choice(blackcube.cloak_3, 1, p = [])
            
            cloak_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.cloak (a+1, b) 

    def belt (a, b):
        if a == b:
            return
        else: 
            belt_op_1 = np.random.choice(blackcube.belt_1, 1, p = [])
            belt_op_2 = np.random.choice(blackcube.belt_2, 1, p = [])
            belt_op_3 = np.random.choice(blackcube.belt_3, 1, p = [])
            
            belt_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.belt (a+1, b) 

    def shoulder (a, b):
        if a == b:
            return
        else: 
            shoulder_op_1 = np.random.choice(blackcube.shoulder_1, 1, p = [])
            shoulder_op_2 = np.random.choice(blackcube.shoulder_2, 1, p = [])
            shoulder_op_3 = np.random.choice(blackcube.shoulder_3, 1, p = [])
            
            shoulder_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.shoulder (a+1, b) 

    def face (a, b):
        if a == b:
            return
        else: 
            face_op_1 = np.random.choice(blackcube.face_1, 1, p = [])
            face_op_2 = np.random.choice(blackcube.face_2, 1, p = [])
            face_op_3 = np.random.choice(blackcube.face_3, 1, p = [])
            
            face_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.face (a+1, b) 

    def eyes (a, b):
        if a == b:
            return
        else: 
            eyes_op_1 = np.random.choice(blackcube.eyes_1, 1, p = [])
            eyes_op_2 = np.random.choice(blackcube.eyes_2, 1, p = [])
            eyes_op_3 = np.random.choice(blackcube.eyes_3, 1, p = [])
            
            eyes_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.eyes (a+1, b) 

    def earring (a, b):
        if a == b:
            return
        else: 
            earring_op_1 = np.random.choice(blackcube.earring_1, 1, p = [])
            earring_op_2 = np.random.choice(blackcube.earring_2, 1, p = [])
            earring_op_3 = np.random.choice(blackcube.earring_3, 1, p = [])
            
            earring_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.earring (a+1, b) 

    def ring (a, b):
        if a == b:
            return
        else: 
            ring_op_1 = np.random.choice(blackcube.ring_1, 1, p = [])
            ring_op_1 = np.random.choice(blackcube.ring_2, 1, p = [])
            ring_op_1 = np.random.choice(blackcube.ring_3, 1, p = [])
            
            ring_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.ring (a+1, b)

    def necklace (a, b):
        if a == b:
            return
        else: 
            necklace_op_1 = np.random.choice(blackcube.necklace_1, 1, p = [])
            necklace_op_2 = np.random.choice(blackcube.necklace_2, 1, p = [])
            necklace_op_3 = np.random.choice(blackcube.necklace_3, 1, p = [])
            
            necklace_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.necklace (a+1, b) 

    def heart (a, b):
        if a == b:
            return
        else: 
            heart_op_1 = np.random.choice(blackcube.heart_1, 1, p = [])
            heart_op_2 = np.random.choice(blackcube.heart_2, 1, p = [])
            heart_op_3 = np.random.choice(blackcube.heart_3, 1, p = [])
            
            heart_result.append(str() + ' ' + str() + ' ' + str())
        blackcube.heart (a+1, b)

class additional:

    #무기_에디 
    wapon_1 = []
    wapon_2 = []
    wapon_3 = []
    #엠블렘_에디 
    emblem_1 = []
    emblem_2 = []
    emblem_3 = []
    #보조무기_에디 
    sub_wapon_1 = []
    sub_wapon_2 = []
    sub_wapon_3 = []
    #포스실드_소울링_에디 
    force_and_soul_1 = []
    force_and_soul_2 = []
    force_and_soul_3 = []
    #방패_에디 
    shield_1 = []
    shield_2 = []
    shield_3 = []
    #모자_에디 
    cap_1 = []
    cap_2 = []
    cap_3 = []
    #상의_에디 
    top_1 = []
    top_2 = []
    top_3 = []
    #한벌옷_에디 
    suit_1 = []
    suit_2 = []
    suit_3 = []
    #하의_에디 
    bottom_1 = []
    bottom_2 = []
    bottom_3 = []
    #신발_에디 
    shoes_1 = []
    shoes_2 = []
    shoes_3 = []
    #장갑_에디 
    gloves_1 = []
    gloves_2 = []
    gloves_3 = []
    #망토_에디 
    cloak_1 = []
    cloak_2 = []
    cloak_3 = []
    #벨트_에디 
    belt_1 = []
    belt_2 = []
    belt_3 = []
    #어깨_에디 
    shoulder_1 = []
    shoulder_2 = []
    shoulder_3 = []
    #얼굴장식_에디 
    face_1 = []
    face_2 = []
    face_3 = []
    #눈장식_에디 
    eyes_1 = []
    eyes_2 = []
    eyes_3 = []
    #귀고리_에디 
    earring_1 = []
    earring_2 = []
    earring_3 = []
    #반지_에디 
    ring_1 = []
    ring_2 = []
    ring_3 = []
    #목걸이_에디 
    necklace_1 = []
    necklace_2 = []
    necklace_3 = []
    #기계심장_에디 
    heart_1 = []
    heart_2 = []
    heart_3 = []

    def wapon (a, b):
        if a == b:
            return
        else: 
            wapon_op_1 = np.random.choice(additional.wapon_1, 1, p = 
            [])
            wapon_op_2 = np.random.choice(additional.wapon_2, 1, p = 
            [])
            wapon_op_3 = np.random.choice(additional.wapon_3, 1, p = 
            [])
            
            wapon_result.append(str(wapon_op_1) + ' ' + str(wapon_op_2) + ' ' + str(wapon_op_3))
        additional.wapon (a+1, b)

    def emblem (a, b):
        if a == b:
            return
        else: 
            emblem_op_1 = np.random.choice(additional.emblem_1, 1, p = 
            [])
            emblem_op_2 = np.random.choice(additional.emblem_2, 1, p = 
            [])
            emblem_op_3 = np.random.choice(additional.emblem_3, 1, p = 
            [])

            emblem_result.append(str(emblem_op_1) + ' ' + str(emblem_op_2) + ' ' + str(emblem_op_3))            
        additional.emblem (a+1, b)

    def sub_wapon (a, b):
        if a == b:
            return
        else: 
            sub_wapon_op_1 = np.random.choice(additional.sub_wapon_1, 1, p = [])
            sub_wapon_op_2 = np.random.choice(additional.sub_wapon_2, 1, p = [])
            sub_wapon_op_3 = np.random.choice(additional.sub_wapon_3, 1, p = [])

            sub_wapon_result.append(str(sub_wapon_op_1) + ' ' + str(sub_wapon_op_2) + ' ' + str(sub_wapon_op_3))    
        additional.sub_wapon (a+1, b)

    def force_and_soul (a, b):
        if a == b:
            return
        else: 
            force_and_soul_op_1 = np.random.choice(additional.force_and_soul_1, 1, p = [])
            force_and_soul_op_2 = np.random.choice(additional.force_and_soul_2, 1, p = [])
            force_and_soul_op_3 = np.random.choice(additional.force_and_soul_3, 1, p = [])

            force_and_soul_result.append(str(force_and_soul_op_1) + ' ' + str(force_and_soul_op_2) + ' ' + str(force_and_soul_op_3))    
        additional.force_and_soul (a+1, b)

    def shield (a, b):
        if a == b:
            return
        else: 
            shield_op_1 = np.random.choice(additional.shield_1, 1, p = [])
            shield_op_2 = np.random.choice(additional.shield_2, 1, p = [])
            shield_op_3 = np.random.choice(additional.shield_3, 1, p = [])

            shield_result.append(str(shield_op_1) + ' ' + str(shield_op_2) + ' ' + str(shield_op_3))        
        additional.shield (a+1, b)

    def cap (a, b):
        if a == b:
            return
        else: 
            cap_op_1 = np.random.choice(additional.cap_1, 1, p = [])
            cap_op_2 = np.random.choice(additional.cap_2, 1, p = [])
            cap_op_3 = np.random.choice(additional.cap_3, 1, p = [])
            
            cap_result.append(str() + ' ' + str() + ' ' + str())
        additional.cap (a+1, b)

    def top (a, b):
        if a == b:
            return
        else: 
            top_op_1 = np.random.choice(additional.top_1, 1, p = [])
            top_op_2 = np.random.choice(additional.top_2, 1, p = [])
            top_op_3 = np.random.choice(additional.top_3, 1, p = [])
            
            top_result.append(str() + ' ' + str() + ' ' + str())
        additional.top (a+1, b)

    def suit (a, b):
        if a == b:
            return
        else: 
            suit_op_1 = np.random.choice(additional.suit_1, 1, p = [])
            suit_op_2 = np.random.choice(additional.suit_2, 1, p = [])
            suit_op_3 = np.random.choice(additional.suit_3, 1, p = [])
            
            suit_result.append(str() + ' ' + str() + ' ' + str())
        additional.suit (a+1, b)

    def bottom (a, b):
        if a == b:
            return
        else: 
            bottom_op_1 = np.random.choice(additional.bottom_1, 1, p = [])
            bottom_op_2 = np.random.choice(additional.bottom_2, 1, p = [])
            bottom_op_3 = np.random.choice(additional.bottom_3, 1, p = [])
            
            bottom_result.append(str() + ' ' + str() + ' ' + str())
        additional.bottom (a+1, b)

    def shoes (a, b):
        if a == b:
            return
        else: 
            shoes_op_1 = np.random.choice(additional.shoes_1, 1, p = [])
            shoes_op_2 = np.random.choice(additional.shoes_2, 1, p = [])
            shoes_op_3 = np.random.choice(additional.shoes_3, 1, p = [])
            
            shoes_result.append(str() + ' ' + str() + ' ' + str())
        additional.shoes (a+1, b) 

    def gloves (a, b):
        if a == b:
            return
        else: 
            gloves_op_1 = np.random.choice(additional.gloves_1, 1, p = [])
            gloves_op_2 = np.random.choice(additional.gloves_2, 1, p = [])
            gloves_op_3 = np.random.choice(additional.gloves_3, 1, p = [])
            
            gloves_result.append(str() + ' ' + str() + ' ' + str())
        additional.gloves (a+1, b)

    def cloak (a, b):
        if a == b:
            return
        else: 
            cloak_op_1 = np.random.choice(additional.cloak_1, 1, p = [])
            cloak_op_2 = np.random.choice(additional.cloak_2, 1, p = [])
            cloak_op_3 = np.random.choice(additional.cloak_3, 1, p = [])
            
            cloak_result.append(str() + ' ' + str() + ' ' + str())
        additional.cloak (a+1, b) 

    def belt (a, b):
        if a == b:
            return
        else: 
            belt_op_1 = np.random.choice(additional.belt_1, 1, p = [])
            belt_op_2 = np.random.choice(additional.belt_2, 1, p = [])
            belt_op_3 = np.random.choice(additional.belt_3, 1, p = [])
            
            belt_result.append(str() + ' ' + str() + ' ' + str())
        additional.belt (a+1, b) 

    def shoulder (a, b):
        if a == b:
            return
        else: 
            shoulder_op_1 = np.random.choice(additional.shoulder_1, 1, p = [])
            shoulder_op_2 = np.random.choice(additional.shoulder_2, 1, p = [])
            shoulder_op_3 = np.random.choice(additional.shoulder_3, 1, p = [])
            
            shoulder_result.append(str() + ' ' + str() + ' ' + str())
        additional.shoulder (a+1, b)

    def face (a, b):
        if a == b:
            return
        else: 
            face_op_1 = np.random.choice(additional.face_1, 1, p = [])
            face_op_2 = np.random.choice(additional.face_2, 1, p = [])
            face_op_3 = np.random.choice(additional.face_3, 1, p = [])
            
            face_result.append(str() + ' ' + str() + ' ' + str())
        additional.face (a+1, b)

    def eyes (a, b):
        if a == b:
            return
        else: 
            eyes_op_1 = np.random.choice(additional.eyes_1, 1, p = [])
            eyes_op_2 = np.random.choice(additional.eyes_2, 1, p = [])
            eyes_op_3 = np.random.choice(additional.eyes_3, 1, p = [])
            
            eyes_result.append(str() + ' ' + str() + ' ' + str())
        additional.eyes (a+1, b)

    def earring (a, b):
        if a == b:
            return
        else: 
            earring_op_1 = np.random.choice(additional.earring_1, 1, p = [])
            earring_op_2 = np.random.choice(additional.earring_2, 1, p = [])
            earring_op_3 = np.random.choice(additional.earring_3, 1, p = [])
            
            earring_result.append(str() + ' ' + str() + ' ' + str())
        additional.earring (a+1, b)

    def ring (a, b):
        if a == b:
            return
        else: 
            ring_op_1 = np.random.choice(additional.ring_1, 1, p = [])
            ring_op_1 = np.random.choice(additional.ring_2, 1, p = [])
            ring_op_1 = np.random.choice(additional.ring_3, 1, p = [])
            
            ring_result.append(str() + ' ' + str() + ' ' + str())
        additional.ring (a+1, b)

    def necklace (a, b):
        if a == b:
            return
        else: 
            necklace_op_1 = np.random.choice(additional.necklace_1, 1, p = [])
            necklace_op_2 = np.random.choice(additional.necklace_2, 1, p = [])
            necklace_op_3 = np.random.choice(additional.necklace_3, 1, p = [])
            
            necklace_result.append(str() + ' ' + str() + ' ' + str())
        additional.necklace (a+1, b) 

    def heart (a, b):
        if a == b:
            return
        else: 
            heart_op_1 = np.random.choice(additional.heart_1, 1, p = [])
            heart_op_2 = np.random.choice(additional.heart_2, 1, p = [])
            heart_op_3 = np.random.choice(additional.heart_3, 1, p = [])
            
            heart_result.append(str() + ' ' + str() + ' ' + str())
        additional.heart (a+1, b)

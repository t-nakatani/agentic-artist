-- contents_advicesテーブルの作成
create table if not exists contents_advices (
    id uuid default uuid_generate_v4() primary key,
    user_id text not null,
    content text not null,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- posting_advicesテーブルの作成
create table if not exists posting_advices (
    id uuid default uuid_generate_v4() primary key,
    user_id text not null,
    content text not null,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- wallet_addressesテーブルの作成
create table if not exists wallet_addresses (
    id uuid default uuid_generate_v4() primary key,
    user_id text not null,
    address text not null,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null,
    unique(user_id)
);

-- インデックスの作成
create index if not exists contents_advices_user_id_idx on contents_advices(user_id);
create index if not exists posting_advices_user_id_idx on posting_advices(user_id);
create index if not exists wallet_addresses_user_id_idx on wallet_addresses(user_id); 
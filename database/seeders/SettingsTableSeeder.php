<?php
namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class SettingsTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        DB::table('settings')->delete();

        $data = [
            ['type' => 'current_session', 'description' => '2023'],
            ['type' => 'system_title', 'description' => 'Utalii'],
            ['type' => 'system_name', 'description' => 'Utalii'],
            ['type' => 'term_ends', 'description' => '08/23/25'],
            ['type' => 'term_begins', 'description' => '08/23/2021'],
            ['type' => 'phone', 'description' => '09123456789'],
            ['type' => 'address', 'description' => 'Dar es Salaam'],
            ['type' => 'system_email', 'description' => 'Otea@otea.com'],
            ['type' => 'alt_email', 'description' => ''],
            ['type' => 'email_host', 'description' => ''],
            ['type' => 'email_pass', 'description' => ''],
            ['type' => 'lock_exam', 'description' => 0],
            ['type' => 'logo', 'description' => ''],
            ['type' => 'next_term_fees_j', 'description' => '20000'],
            ['type' => 'next_term_fees_pn', 'description' => '25000'],
            ['type' => 'next_term_fees_p', 'description' => '25000'],
            ['type' => 'next_term_fees_n', 'description' => '25600'],
            ['type' => 'next_term_fees_s', 'description' => '15600'],
            ['type' => 'next_term_fees_c', 'description' => '1600'],
        ];

        DB::table('settings')->insert($data);

    }
}

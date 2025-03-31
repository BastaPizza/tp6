<?php
/**
 * PHP version 8.3
 *
 * Classe MesDates
 *
 * Cette classe fournit des méthodes pour obtenir des dates, comme la date de demain.
 *
 * @category DateTime
 * @package  UPJV
 * @author   Fourdrain <corentinfrdr@gmail.com>
 * @license  https://opensource.org/licenses/MIT MIT
 * @link     http://www.exemple.com
 */

namespace UPJV;

/**
 * Class MesDates
 *
 * Fournit des méthodes pour manipuler des dates.
 *
 * @category DateTime
 * @package  UPJV
 * @author   Fourdrain <corentinfrdr@gmail.com>
 * @license  https://opensource.org/licenses/MIT MIT
 * @link     http://www.exemple.com
 */
class MesDates
{
    /**
     * Retourne la date de demain au format JJ-MM-AAAA.
     *
     * @return string La date de demain sous forme de chaîne JSON.
     */
    public function demain()
    {
        $demain = new \DateTime();
        $demain->modify('+1 day');

        return json_encode(['demain' => $demain->format('d-m-Y')]);
    }
}

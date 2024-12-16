import { getDate, getMonth, getYear } from 'https://cdn.jsdelivr.net/npm/bangla-calendar@7.0.0/+esm';
        const getFormattedDate = () => {
            const today = new Date();
            const options = { year: 'numeric', month: 'long', day: 'numeric' };

            const banglaDigits = {
                0: '০', 1: '১', 2: '২', 3: '৩', 4: '৪',
                5: '৫', 6: '৬', 7: '৭', 8: '৮', 9: '৯'
            };
            const formatNumberToBangla = (number) =>
                number.toString().replace(/[0-9]/g, (digit) => banglaDigits[digit]);

            const formattedDate = today.toLocaleDateString('bn-BD', options);
            return formatNumberToBangla(formattedDate);
        };
        const date1 = new Date();
        const banglaDate = getDate(date1); // Returns day in Bangla
        const banglaFormattedDate = `${banglaDate}`;

        document.getElementById("gregorian-date").innerText = getFormattedDate(); // Set Gregorian date
        document.getElementById("bangla-date").innerText = banglaFormattedDate; // Set Bangla date